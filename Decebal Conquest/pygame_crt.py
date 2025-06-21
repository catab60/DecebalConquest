import struct
from typing import Optional, Tuple
import os
os.environ["KIVY_GL_BACKEND"] = 'angle_sdl2'

import pygame
import zengl


class CRTScreen:
    def __init__(self, screen_size: Tuple[int, int], window_size: Tuple[int, int]):
        self.window_size = tuple(window_size)
        self.screen_size = tuple(screen_size)
        self.screen_aspect = self.screen_size[0] / self.screen_size[1]

        self.ctx = zengl.context()
        self.image = self.ctx.image(self.screen_size, "rgba8unorm")
        self.output = self.ctx.image(self.window_size, "rgba8unorm")
        self.pipeline = self.ctx.pipeline(
            vertex_shader="""
                #version 300 es
                precision highp float;

                uniform vec2 offset;
                uniform vec2 scale;

                vec2 vertices[4] = vec2[](
                    vec2(-1.0, -1.0),
                    vec2(-1.0, 1.0),
                    vec2(1.0, -1.0),
                    vec2(1.0, 1.0)
                );

                out vec2 vertex;

                void main() {
                    gl_Position = vec4(vertices[gl_VertexID], 0.0, 1.0);
                    vertex = (vertices[gl_VertexID] + offset) * scale;
                }
            """,
            fragment_shader="""
                #version 300 es
                precision highp float;

                uniform float color_shift;
                uniform int color_mode;
                uniform int enable_noise;
                uniform int enable_scanline;
                uniform int enable_multisample;
                uniform int enable_screen;

                uniform float time;
                uniform vec2 screen_size;
                uniform sampler2D Texture;

                in vec2 vertex;
                out vec4 out_color;

                float hash13(vec3 p3) {
                    p3 = fract(p3 * 0.1031);
                    p3 += dot(p3, p3.zyx + 31.32);
                    return fract((p3.x + p3.y) * p3.z);
                }

                vec2 hash23(vec3 p3) {
                    p3 = fract(p3 * vec3(0.1031, 0.1030, 0.0973));
                    p3 += dot(p3, p3.yzx + 33.33);
                    return fract((p3.xx + p3.yz) * p3.zy);
                }

                vec3 aces(vec3 x) {
                    const float a = 2.51;
                    const float b = 0.03;
                    const float c = 2.43;
                    const float d = 0.59;
                    const float e = 0.14;
                    return clamp((x * (a * x + b)) / (x * (c * x + d) + e), 0.0, 1.0);
                }

                vec3 sample_screen(vec2 uv) {
                    if (color_shift == 0.0) {
                        return texture(Texture, uv).bgr;
                    }
                    return vec3(
                        texture(Texture, uv - color_shift).b,
                        texture(Texture, uv).g,
                        texture(Texture, uv + color_shift).r
                    );
                }

                vec3 screen(vec2 vertex) {
                    if (abs(vertex.x) > 1.001 || abs(vertex.y) > 1.001) {
                        return vec3(0.161,0.141,0.22);
                    }
                    vec2 uv = vertex * 0.5 + 0.5;
                    uv.y = 1.0 - uv.y;
                    vec3 color = sample_screen(uv);
                    if (enable_noise == 1) {
                        float noise = hash13(floor(vec3(uv * screen_size, floor(time))));
                        color *= 1.0 + (noise - 0.5) * 0.1;
                    }
                    if (enable_scanline == 1) {
                        float scanline = sin(uv.y * screen_size.y * 3.141592 + time * 0.05) * 0.25 + 1.0;
                        color *= scanline;
                    }
                    if (color_mode == 1) {
                        color = color * 1.05 + 0.05;
                    }
                    if (color_mode == 2) {
                        color = aces(color);
                    }
                    return color;
                }

                void main() {
                    if (enable_screen == 0) {
                        if (abs(vertex.x) <= 1.0 || abs(vertex.y) <= 1.0) {
                            vec2 uv = vertex * 0.5 + 0.5;
                            uv.y = 1.0 - uv.y;
                            out_color = texture(Texture, uv).bgra;
                        } else {
                            out_color = vec4(0.0, 0.0, 0.0, 1.0);
                        }
                        return;
                    }
                    vec2 v = vertex * (1.0 + pow(abs(vertex.yx), vec2(2.0)) * 0.15);
                    vec3 color = vec3(0.0);
                    if (enable_multisample == 1) {
                        for (int i = 0; i < 16; ++i) {
                            vec2 offset = hash23(vec3(v * screen_size, float(i))) - 0.5;
                            color += screen(v * 1.01 + offset / screen_size);
                        }
                        color /= 16.0;
                    } else {
                        color = screen(v * 1.01);
                    }
                    out_color = vec4(color, 1.0);
                }
            """,
            layout=[
                {
                    "name": "Texture",
                    "binding": 0,
                },
            ],
            resources=[
                {
                    "type": "sampler",
                    "binding": 0,
                    "image": self.image,
                    "min_filter": "nearest",
                    "mag_filter": "nearest",
                    "wrap_x": "clamp_to_edge",
                    "wrap_y": "clamp_to_edge",
                },
            ],
            uniforms={
                "time": 0.0,
                "scale": (1.0, 1.0),
                "offset": (0.0, 0.0),
                "screen_size": self.screen_size,
                "color_shift": 0.001,
                "color_mode": 1,
                "enable_noise": 1,
                "enable_scanline": 1,
                "enable_multisample": 1,
                "enable_screen": 1,
            },
            framebuffer=[self.output],
            topology="triangle_strip",
            vertex_count=4,
        )

#return vec3(0.192,0.173,0.243);

    def configure(
        self,
        color_shift: Optional[float] = None,
        color_mode: Optional[str] = None,
        enable_noise: Optional[bool] = None,
        enable_scanline: Optional[bool] = None,
        enable_multisample: bool = None,
        enable_screen: Optional[bool] = None,
    ):
        if color_shift is not None:
            color_shift = min(max(float(color_shift), -0.01), 0.01)
            self.pipeline.uniforms["color_shift"][:] = struct.pack("i", color_shift)
        if color_mode is not None:
            color_mode = ["none", "bright", "aces"].index(color_mode)
            self.pipeline.uniforms["color_mode"][:] = struct.pack("i", color_mode)
        if enable_noise is not None:
            enable_noise = int(bool(enable_noise))
            self.pipeline.uniforms["enable_noise"][:] = struct.pack("i", enable_noise)
        if enable_scanline is not None:
            enable_scanline = int(bool(enable_scanline))
            self.pipeline.uniforms["enable_scanline"][:] = struct.pack("i", enable_scanline)
        if enable_multisample is not None:
            enable_multisample = int(bool(enable_multisample))
            self.pipeline.uniforms["enable_multisample"][:] = struct.pack("i", enable_multisample)
        if enable_screen is not None:
            enable_screen = int(bool(enable_screen))
            self.pipeline.uniforms["enable_screen"][:] = struct.pack("i", enable_screen)

    def render(
        self,
        screen: pygame.surface.Surface,
        offset: Optional[Tuple[float, float]] = None,
        tick: Optional[float] = None,
    ):
        if offset is None:
            offset = (0.0, 0.0)

        if tick is None:
            tick = pygame.time.get_ticks()

        window_width, window_height = pygame.display.get_window_size()
        window_aspect = window_width / window_height
        offset_x, offset_y = offset[0] / self.screen_size[0], offset[1] / self.screen_size[1]
        scale_x, scale_y = 1.0, 1.0

        if self.screen_aspect < window_aspect:
            scale_x = window_aspect / self.screen_aspect
        else:
            scale_y = self.screen_aspect / window_aspect

        self.ctx.new_frame()
        view = screen.get_buffer()
        self.image.write(view)
        self.pipeline.viewport = (0, 0, window_width, window_height)
        self.pipeline.uniforms["time"][:] = struct.pack("f", tick)
        self.pipeline.uniforms["scale"][:] = struct.pack("2f", scale_x, scale_y)
        self.pipeline.uniforms["offset"][:] = struct.pack("2f", offset_x, offset_y)
        self.pipeline.render()
        self.output.blit()
        self.ctx.end_frame()

    def screenshot(self) -> pygame.surface.Surface:
        return pygame.image.frombytes(self.output.read(), self.window_size, 'RGBA')

    def release(self):
        self.ctx.release(self.pipeline)
        self.ctx.release(self.image)
        self.pipeline = None
        self.image = None
