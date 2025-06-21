import pygame
import sys
import math
from pygame_crt import CRTScreen
from PIL import Image, ImageTk
import tkinter as tk
import win32gui
import win32con
import win32api
import keyboard
import time
import random
import os
import numpy as np
import pyaudio



'''
def on_key_press(event):
    if event.char == "w":
        player.move_forward()
'''

SAMPLE_RATE = 44100
CHUNK_SIZE = 1024
THRESHOLD = 0.01
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=SAMPLE_RATE,
                 input=True,
                 frames_per_buffer=CHUNK_SIZE)

class Player:

    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.speed = 10
        self.body = pygame.Rect(self.x,self.y,50,50) 


    def draw(self, screen,color):
        self.body = pygame.Rect(self.x,self.y,50,50) 
        pygame.draw.rect(screen,color,self.body)

class Background():
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.images = images
        self.image_index = 0
    def draw(self, window):
        image = self.images[self.image_index]
        body = image.get_rect(center=(self.x, self.y))
        window.blit(image, body.topleft)
    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)

class Earth():
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.images = images
        self.image_index = 0
        self.body = None
    def draw(self, window):
        image = self.images[self.image_index]
        self.body = image.get_rect(center=(self.x, self.y))
        window.blit(image, self.body.topleft)
    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)

class Spaceship:
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 10
        self.images = images
        self.image_index = 0
        self.rotated_rect = None
        self.health = 10

    def rotate(self, direction):
        if direction == 'left':
            self.angle -= 5
        elif direction == 'right':
            self.angle += 5



    def move_forward(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
        #self.body = pygame.(self.x,self.y,50,50)
    
    def move_back(self):
        self.x -= self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self, window):
        self.rotated_image = pygame.transform.rotate(self.images[self.image_index], self.angle)
        self.rotated_rect = self.rotated_image.get_rect(center=(self.x, self.y))
        window.blit(self.rotated_image, self.rotated_rect.topleft) 

    def shoot(self):
        if loud:
            self.projectile=Projectile(self.x,self.y,self.angle, power_images)
        else:
            self.projectile=Projectile(self.x,self.y,self.angle, proj_images)
        projArr.append(self.projectile)


    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)

pygame.init()

screen_width = 800
screen_height = 600

HasMinigun = False
HasShield = False
HasBullet = False
HasWolf = False
defeatDecebal = False
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

screen = pygame.surface.Surface((screen_width, screen_height))
pygame.display.set_mode((screen_width, screen_height), flags=pygame.OPENGL | pygame.NOFRAME)
final_screen = CRTScreen((screen_width, screen_height), (screen_width, screen_height))
pygame.display.set_caption("spaceship")

spaceship_images = []
for i in range(30):
    original_image = pygame.image.load(f"rend/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.4, original_image.get_height() * 0.4))
    spaceship_images.append(scaled_image)

spaceship2_images = []
for i in range(30):
    original_image = pygame.image.load(f"rend2/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.4, original_image.get_height() * 0.4))
    spaceship2_images.append(scaled_image)

earth_images = []
for i in range(60):
    original_image = pygame.image.load(f"eatr/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.8, original_image.get_height() * 0.8))
    earth_images.append(scaled_image)

alien_images = []
for i in range(40):
    original_image = pygame.image.load(f"alien/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.3, original_image.get_height() * 0.3))
    alien_images.append(scaled_image)

proj_images = []
for i in range(20):
    original_image = pygame.image.load(f"poj/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.1, original_image.get_height() * 0.1))
    proj_images.append(scaled_image)

black_images = []
for i in range(20):
    original_image = pygame.image.load(f"spartn/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.5, original_image.get_height() * 0.5))
    black_images.append(scaled_image)

coin_images = []
for i in range(40):
    original_image = pygame.image.load(f"coin/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.5, original_image.get_height() * 0.5))
    coin_images.append(scaled_image)

decebal_images = []
for i in range(40):
    original_image = pygame.image.load(f"dece/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.5, original_image.get_height() * 0.5))
    decebal_images.append(scaled_image)

fireball_images = []
for i in range(20):
    original_image = pygame.image.load(f"firebal/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.2, original_image.get_height() * 0.2))
    fireball_images.append(scaled_image)

power_images = []
for i in range(20):
    original_image = pygame.image.load(f"power/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.2, original_image.get_height() * 0.2))
    power_images.append(scaled_image)

cesar_images = []
for i in range(40):
    original_image = pygame.image.load(f"cesar/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.5, original_image.get_height() * 0.5))
    cesar_images.append(scaled_image)





def spawnRandomBH():
    xa=random.randint(50,350)
    xb=random.randint(500,750)
    ya=random.randint(50,550)
    a = random.randint(1,2)

    if a == 1:
        return BlackHole(xb,ya, black_images)
    else:
        return BlackHole(xa,ya, black_images)


font = pygame.font.Font("font1.ttf", 50)
font1 = pygame.font.Font("font1.ttf", 20)
font2 = pygame.font.Font("font1.ttf", 10)
bg_images = []
for i in range(100):
    original_image = pygame.image.load(f"bg/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 1.3, original_image.get_height() * 2.0))
    bg_images.append(scaled_image)


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def on_mouse_motion(event):
    global x, y
    x = event.x
    y = event.y

class pyButtonGIF():
    def __init__(self, x, y, image, scale, folder):
        self.imageArgs = image
        image.set_alpha(100)
        self.scaleArgs = scale
        self.speed = 0.05
        self.constscalseArgs = scale
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.state_left = win32api.GetKeyState(0x01)

        all_files = []
        self.gifImages = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                all_files.append(file_path)
        
        all_files = sorted(files, key=lambda x: int(x.split('.')[0]))
    

        for file in all_files:
            self.gifImages.append(pygame.image.load(f"{folder}/{file}"))

        self.k = 0
        self.kk = 0
        

    def draw(self, surface, xo, yo):
        
        action = False

        pos = (x,screen_height-y)
          

        a = win32api.GetKeyState(0x01)

        if self.rect.collidepoint(pos[0]+xo, pos[1]-yo):
            self.scaleArgs += self.speed
            self.changeImage(self.gifImages[self.k], self.scaleArgs*100+100)
            if self.kk == 2:
                self.k += 1
                self.kk = 0
            self.kk+=1
            if self.k >= len(self.gifImages)-1:
                self.k = 0
            if self.scaleArgs <= self.constscalseArgs+0.1:
                self.imageArgs.set_alpha(self.scaleArgs*100+100)
                self.image = pygame.transform.scale(self.imageArgs, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))
            else:
                self.scaleArgs = self.constscalseArgs+0.1
            if a!= self.state_left:
                self.state_left = a
                if a < 0 and self.clicked == False:
                    self.clicked = True
                    action = True
                else:
                    self.clicked = False
        else:
            self.k = 0
            self.changeImage(self.gifImages[self.k], self.scaleArgs*100+50)
            if self.scaleArgs >= self.constscalseArgs:
                self.scaleArgs -= self.speed
                self.imageArgs.set_alpha(self.scaleArgs*100+50)
                self.image = pygame.transform.scale(self.imageArgs, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))


        #draw button on screen
        self.rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, (self.rect.x, self.rect.y), )

        return action
    
    def changeImage(self, image, alpha):
        self.imageArgs = image
        image.set_alpha(alpha)
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))

class pyAnimatedOBJ():
    def __init__(self, image, scale, folder):
        self.scaleArgs = scale
        all_files = []
        self.gifImages = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                all_files.append(file_path)

        all_files = sorted(files, key=lambda x: int(x.split('.')[0]))

        self.k = 0
        self.kk = 0
        self.imageArgs = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        

        for file in all_files:
            self.gifImages.append(pygame.image.load(f"{folder}/{file}"))

    def draw(self, surface, x, y, alpha):

        self.changeImage(self.gifImages[self.k], alpha)

        if self.kk == 2:
                self.k += 1
                self.kk = 0
        self.kk+=1
        if self.k >= len(self.gifImages):
            self.k = 0

        self.rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, (x,y))

    def changeImage(self, image, alpha):
        self.imageArgs = image
        image.set_alpha(alpha)
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))

coinArr = []

class Coing:
    def __init__(self, x, y, images): 
        self.x=x
        self.y=y
        self.speed = 3
        self.angle = 0
        self.images = images
        self.image_index = 0
        self.body = pygame.Rect(self.x,self.y,25,25) 

    def draw(self, screen ,color):

        image = self.images[self.image_index]
        self.body = image.get_rect(center=(self.x, self.y))
        screen.blit(image, self.body)

    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)

    def attract(self,x1,y1):
        
        dx = x1 - self.x
        dy = y1 - self.y
        self.angle = math.atan2(dy,dx)

        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)

        self.x += dx
        self.y += dy

followArr = []

isP2 = True
wasCesar = False
class Projectile:
    def __init__(self,x,y,angle,images) :
        self. x = x
        self. y = y
        self. angle = angle
        self.speed =  30
        self.images = images
        self.image_index = 0
        self.body = pygame.Rect(self.x,self.y,20,20)
        self.SpawnCoin = True
        self.id =0
        


    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        
    def followingBullet(self,screen,color,k):
        global defeatDecebal
        if self.id == 1 :

            dx = player.x - self.x
            dy = player.y - self.y
            
            self.angle = math.atan2(dy,dx)
            self.speed = 4
            dx = self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            
            self.x += dx
            self.y += dy

            if self.body.colliderect(player.rotated_rect) or self.body.colliderect(player2.rotated_rect):
                followArr.pop(k)
            
            image = self.images[self.image_index]
            self.body = image.get_rect(center=(self.x, self.y))
            screen.blit(image, self.body)
        
        elif self.id == 2 :
            dx = player2.x - self.x
            dy = player2.y - self.y
            
            self.angle = math.atan2(dy,dx)
            self.speed = 4
            dx = self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            
            self.x += dx
            self.y += dy
            if self.body.colliderect(player2.rotated_rect) or self.body.colliderect(player.rotated_rect):
                followArr.pop(k)
            
            image = self.images[self.image_index]
            self.body = image.get_rect(center=(self.x, self.y))
            screen.blit(image, self.body)
        
        



    def draw(self,screen,color,astro,k):
        global score, defeatDecebal
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

        for i in range( len(astro)):
            if not astro[i].Destroyed:
                if self.x>850 or self.x<0 or self.y>650 or self.y<0:
                    projArr.pop(k)
                    return 0
                if self.body.colliderect(astro[i].body):

                    if astro[i].health> 0:
                        if HasBullet:
                            astro[i].health -= 2
                        else:
                            astro[i].health -= 1
                        projArr.pop(k)
                    else:
                        
                        

                        astro[i].death(astro,i)
                        if astro[i].name == "decebal":
                            defeatDecebal = True
                            
                        projArr.pop(k)
                        score+=1
        

        image = self.images[self.image_index]
        self.body = image.get_rect(center=(self.x, self.y))
        screen.blit(image, self.body)




death_effect = []

class BlackHole:

    def __init__(self,x,y, images) :
        self.x = x
        self.y = y
        self.images = images
        self.image_index = 0
    
        self.body = pygame.Rect(self.x,self.y,50,50) 

    def draw(self, screen,color):
        image = self.images[self.image_index]
        self.body = image.get_rect(center=(self.x-50, self.y-50))
        screen.blit(image, self.body)


    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)





for i in range(60):
    original_image = pygame.image.load(f"deathEffect/{i+1}.png")
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * 0.2, original_image.get_height() * 0.2))
    death_effect.append(scaled_image)
class Asteroid:
     
    def __init__(self,x,y,sizex,sizey,images) :#px1= planeta x py1 planeta y
        self.id = 0
        self.asteroidx = x
        self.asteroidy = y
        self.offset = random.randint(1,20)
        self.asteroidSizex = sizex
        self.asteroidSizey = sizey
        self.speed = 2
        self.health = 2
        self.images = images
        self.image_index = 0
        self.Destroyed = False
        self.name = ""
        self.body = pygame.Rect(self.asteroidx , self.asteroidy , self.asteroidSizex , self.asteroidSizey)

    def blip(self): 
        xa = random.randint(50,750)
        ya = random.randint(50,550)
        self.asteroidx = xa
        self.asteroidy = ya
        '''ya = random.randint(0,550)
        yb = random.randint(0,500)

        xc = random.randint(50,750)
        yc = random.randint(50,550)
        a = random.randint(1,8)
        if a == 1:
            self.asteroidx = xa 
            self.asteroidy = ya 
        elif a == 2 :
            self.asteroidx = xa 
            self.asteroidy = yb 
        elif a == 3 :
            self.asteroidx = xb 
            self.asteroidy = ya 
        elif a == 4 :
            self.asteroidx = xb 
            self.asteroidy = yb  
        elif a == 5 :
            self.asteroidx = xc 
            self.asteroidy = ya 
        elif a == 6 :
            self.asteroidx = xc 
            self.asteroidy = yb 
        elif a == 7 :
            self.asteroidx = xa 
            self.asteroidy = yc 
        elif a == 8:
            self.asteroidx = xb 
            self.asteroidy = yc'''
        


        self.body = pygame.Rect(self.asteroidx , self.asteroidy , self.asteroidSizex , self.asteroidSizey)

    def death(self, astro,i):
        if not self.Destroyed:
            self.images = death_effect
            self.image_index = 0
            self.Destroyed= True
            coinn = Coing(self.asteroidx-35,self.asteroidy-35, coin_images)
            coinArr.append(coinn)
            death_sound.play()
        
    def get_health(self):
        return self.health
            
            

      
 
    def calcDist(self,px1,px2):
        
        self.distance_from_centre = math.sqrt((px1  - self.asteroidx) ** 2 + (px2 - self.asteroidy) ** 2)

    def moveFibo(self,x1,x2):
        self.speed = 0.2
        if not self.Destroyed:
            angle = pygame.time.get_ticks() / 1000 * self.speed  + self.offset
            self.asteroidx = x1 + self.distance_from_centre * math.cos(angle)
            self.asteroidy = x2 + self.distance_from_centre * math.sin(angle)

            self.distance_from_centre = math.sqrt((x1  - self.asteroidx) ** 2 + (x2 - self.asteroidy) ** 2)

            if self.distance_from_centre > 50/2:
                self.distance_from_centre -= 0.5

    def moveStraight(self,x1,y1):
        if not self.Destroyed:
            dx = x1 - self.asteroidx
            dy = y1 - self.asteroidy
            self.angle = math.atan2(dy,dx)

            dx = self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)

            self.asteroidx += dx
            self.asteroidy += dy

    
    def draw(self, screen,color):

        image = self.images[self.image_index]
        self.body = image.get_rect(center=(self.asteroidx, self.asteroidy))
        screen.blit(image, self.body)


    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)



class pyButton():
    def __init__(self, x, y, image, scale, speed):
        self.imageArgs = image
        image.set_alpha(100)
        self.scaleArgs = scale
        self.speed = speed
        self.constscalseArgs = scale
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.state_left = win32api.GetKeyState(0x01)

    def draw(self, surface, alpha_0, alpha_1, x_offset, y_offset, size):
        action = False
        pos = (x,screen_height-y)
        a = win32api.GetKeyState(0x01)
        if self.rect.collidepoint((pos[0]+x_offset, pos[1]+y_offset))==False:
            self.image.set_alpha(alpha_0)
        if self.rect.collidepoint((pos[0]+x_offset, pos[1]+y_offset)):
            self.scaleArgs += self.speed
            if self.scaleArgs <= self.constscalseArgs+size:
                self.imageArgs.set_alpha(alpha_1)
                self.image = pygame.transform.scale(self.imageArgs, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))
            else:
                self.scaleArgs = self.constscalseArgs+size
            if a!= self.state_left:
                self.state_left = a
                if a < 0 and self.clicked == False:
                    self.clicked = True
                    action = True
                else:
                    self.clicked = False
        else:
            if self.scaleArgs >= self.constscalseArgs:
                self.scaleArgs -= self.speed
                self.imageArgs.set_alpha(alpha_0)
                self.image = pygame.transform.scale(self.imageArgs, (int(self.width * self.scaleArgs), int(self.height * self.scaleArgs)))

        
        #draw button on screen
        self.rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, (self.rect.x, self.rect.y), )

        return action


def spawnRandomSt(gid):
    xa = random.randint(-200,0)
    xb = random.randint(850,1100)
    ya = random.randint(-200,0)
    yb = random.randint(850,1100)

    xc = random.randint(0,800)
    yc = random.randint(0,600)
    
    a = random.randint(1,8)

    if a == 1:
        asteroi = Asteroid(xa,ya,50,50, alien_images)
    elif a == 2 :
        asteroi = Asteroid(xa,yb,50,50, alien_images)
    elif a == 3 :
        asteroi = Asteroid(xb,ya,50,50, alien_images)
    elif a == 4 :
        asteroi = Asteroid(xb,yb,50,50, alien_images)
    elif a == 5 :
        asteroi = Asteroid(xc,ya,50,50, alien_images)
    elif a == 6 :
        asteroi = Asteroid(xc,yb,50,50, alien_images)
    elif a == 7 :
        asteroi = Asteroid(xa,yc,50,50, alien_images)
    elif a == 8:
        asteroi = Asteroid(xb,yc,50,50, alien_images)
    asteroi.id = gid
    return asteroi

earthShadow = pygame.image.load("eatr_shadow.png")
earthShadow = pygame.transform.scale(earthShadow, (earthShadow.get_width() * 0.8, earthShadow.get_height() * 0.8))
earthShadow_rect = earthShadow.get_rect()
earthShadow_rect.center = (screen_width // 2, screen_height // 2)



projArr = []
player=Spaceship(100,100, spaceship_images)
player2=Spaceship(100,300, spaceship2_images)
earth = Earth(400,300, earth_images)
bg = Background(400,300, bg_images)
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (logo.get_width() * 3.0, logo.get_height() * 3.0))

x,y = 0,0

logoAlpha = 0

asteroidArr = []




PlayButton_image = pygame.image.load("play.png")
PlayButton = pyButton(400,150, PlayButton_image, 0.65, 0.01)

CloseButton_image = pygame.image.load("Close.png")
CloseButton = pyButton(730,510, CloseButton_image, 0.65, 0.01)


CloseMainButton = pyButton(760,560, CloseButton_image, 0.65, 0.01)

ExitButton_image = pygame.image.load("exit.png")
ExitButton = pyButton(400,70, ExitButton_image, 0.65, 0.01)

BuyButton_image = pygame.image.load("Buy.png")
Buy1Button = pyButton(310,335, BuyButton_image, 0.4, 0.01)
Buy2Button = pyButton(310,150, BuyButton_image, 0.4, 0.01)
Buy3Button = pyButton(650,335, BuyButton_image, 0.4, 0.01)
Buy4Button = pyButton(650,150, BuyButton_image, 0.4, 0.01)


Border = pygame.image.load("outline.png")
ShopGUI = pygame.image.load("shopGUI.png")
InfoGUI = pygame.image.load("tutGUI.png")
Check = pygame.image.load("check.png")
Prot = pygame.image.load("prot.png")

he1 = pygame.image.load("he1.png")
he2 = pygame.image.load("he2.png")


WinGUI = pygame.image.load("win.png")
LoseGUI = pygame.image.load("lost.png")


Shop = pyButtonGIF(750,50, Border, 0.48, "ShopIcon")
Info = pyButtonGIF(50,50, Border, 0.48, "tut")

Minigun = pyAnimatedOBJ(CloseButton_image, 0.5, "minigun")
Protection = pyAnimatedOBJ(CloseButton_image, 0.5, "shield")
Bullet = pyAnimatedOBJ(CloseButton_image, 0.5, "bullet")
Lup = pyAnimatedOBJ(CloseButton_image, 0.5, "wolf")
Coin = pyAnimatedOBJ(CloseButton_image, 1.0, "coin")

Heart = pyAnimatedOBJ(CloseButton_image, 0.2, "heart")

logoim = pygame.image.load("logobig.png")  # Replace "image.png" with the path to your image file
logoim_rect = logoim.get_rect(center=(screen_width // 2, screen_height // 2))

show_screen = 0
frameCounter = 0
ProjSpeed = 10
score = 0
coins = 2000
fade_in = True
isHole = False
heartVal = 100.0
blk = BlackHole(250,250, black_images)
spawnedDecebal = False

shoot_effect = pygame.mixer.Sound("shot.wav")
coin_effect = pygame.mixer.Sound("coin.wav")
death_sound = pygame.mixer.Sound("death.wav")

countdown = False
countdownStart = False
waveCount = 0
CurWep=1
CurrentWeapon = 1
def update_game():
    global show_screen
    global frameCounter
    global HasMinigun
    global HasShield
    global HasBullet
    global HasWolf
    global ProjSpeed
    global proj_images
    global power_images
    global score
    global coins
    global logoAlpha
    global fade_in
    global isHole
    global heartVal
    global countdown
    global countdownStart
    global waveCount
    global loud
    global CurWep
    global wasCesar
    global defeatDecebal
    global spawnedDecebal
    while True:

        audio_data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)
        rms = np.sqrt(np.mean(np.square(audio_data)))
    
        


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    pygame.mixer.music.stop()
                except:
                    pass
                sys.exit()
        if keyboard.is_pressed("a"):
            player.rotate("left")
        
        if keyboard.is_pressed("d"):
            player.rotate("right")

        if keyboard.is_pressed("w"):
            player.move_forward()

            if player.x < -50 or player.y < -50 or player.x >850 or player.y >650:
                player.move_back()
        if keyboard.is_pressed("s"):
            player.move_back()
            if player.x < -50 or player.y < -50 or player.x >850 or player.y >650:
                player.move_forward()

        if keyboard.is_pressed("e"):
            if frameCounter % ProjSpeed == 0:
                if player.health>0:
                    player.shoot()
                    shoot_effect.play()
        if keyboard.is_pressed("p") and len(asteroidArr)==0:
            countdownStart = True
            countdown=1
        if keyboard.is_pressed("1"):
            CurWep = 1
        if keyboard.is_pressed("2"):
            if HasMinigun:
                CurWep = 2

        if CurWep ==1:
            ProjSpeed=10
        elif CurWep ==2:
            ProjSpeed=5

        if rms > THRESHOLD:
            loud = False
            if CurWep!=2:
                ProjSpeed = 10
            
        else:
            loud = True
            ProjSpeed = 1



        if keyboard.is_pressed("g"):
            player2.rotate("left")
        if keyboard.is_pressed("j"):
            player2.rotate("right")
        if keyboard.is_pressed("y"):
            player2.move_forward()
        if keyboard.is_pressed("h"):
            player2.move_back()
        if keyboard.is_pressed("u"):
            if frameCounter % ProjSpeed == 0:
                if player2.health>0:
                    player2.shoot()
                    shoot_effect.play()

        if keyboard.is_pressed("6"):
            ProjSpeed = 10
        if keyboard.is_pressed("7"):
            if HasMinigun:
                ProjSpeed = 5


        screen.fill((255, 255, 255))

        try:
            if frameCounter % 90 == 0 and waveCount == 10 and spawnedDecebal == True or frameCounter%90 ==0 and waveCount == 5 and wasCesar == True :
                    
                pog = Projectile(asteroidArr[0].asteroidx,asteroidArr[0].asteroidy,1, fireball_images)

                if isP2 == True and pog.id == 0:
                    pog.id = random.randint(1,2)
                    

                elif pog.id == 0:
                    pog.id = 1 

                followArr.append(pog)

        except Exception as f:
            print(f)

        try:
            for i in range(len(followArr)):
                for j in range(len(projArr)):
                    if followArr[i].body.colliderect(projArr[j].body):
                        followArr.pop(i)
                        projArr.pop(j)
        except:
            pass

        

        # Determine if the audio is loud or quiet
        
            

        if show_screen == 0:
            bg.draw(screen)
            bg.update()

            screen.blit(logo, (110, math.ceil(math.sin(time.time()*2)*20)+250))
            screen.blit(Border,(0,0))

            if PlayButton.draw(screen, 200, 100, 0,0, 0.05):
                show_screen = 1
        
            if ExitButton.draw(screen, 200, 100, 0,0, 0.05):
                pygame.quit()
                try:
                    pygame.mixer.music.stop()
                except:
                    pass
                sys.exit()

            if Info.draw(screen,-40, 20):
                show_screen=3

        if show_screen == 1 or show_screen ==2 or show_screen == 3:
            bg.draw(screen)
            bg.update()
            if player.health>0:
                player.draw(screen)
                player.update()
            if player2.health>0:
                player2.draw(screen)
                player2.update()
            screen.blit(earthShadow, earthShadow_rect)
            earth.draw(screen)
            earth.update()

            if HasShield:
                screen.blit(Prot, (296,196))

            try:

                for i in range(len(followArr)):
                    if followArr[i].body.colliderect(player.rotated_rect):
                        player.health -= 1
                        
                    elif followArr[i].body.colliderect(player2.rotated_rect):
                        player2.health -=1
            

                    followArr[i].followingBullet(screen,(255,0,0),i)
                    followArr[i].update()

                    
            except:
                pass


            
            for i in range(player.health):
                screen.blit(he1,(20*i+20,500))
            for i in range(player2.health):
                screen.blit(he2,(20*i+20,520))


        
            
            if countdownStart ==True:
                countdown += 1
                
            
            if countdownStart == True and countdown % 10 == 0:

                if waveCount == 10 :
                    
                    astroId = 1
                    asteroi = Asteroid(0,200,200,200,decebal_images)
                    asteroi.speed = 1
                    asteroi.name = "decebal"
                    asteroi.health=100
                    asteroi.id=astroId
                    spawnedDecebal = True
                    asteroi.calcDist(earth.x,earth.y)
                    asteroidArr.append(asteroi)
                    countdownStart = False
                
                elif waveCount == 5 and wasCesar == False:
                    astroId = 3
                    asteroi = Asteroid(0,200,200,200, cesar_images)
                    asteroi.name="cesar"
                    asteroi.health=50
                    asteroi.id=astroId
                    wasCesar = True
                    asteroi.calcDist(earth.x,earth.y)
                    asteroidArr.append(asteroi)
                    countdownStart = False
                    
                elif wasCesar == True and waveCount == 5:
                    
                    for i in range(waveCount*2):

                        astroId = random.randint(1,2)#COUNTDOWN
                        if astroId == 1:

                            asteroi = Asteroid(10,10,50,50, alien_images)#ASTEROID ID
                            asteroi.id=astroId

                        else:

                            asteroi = spawnRandomSt(astroId)

                        asteroi.calcDist(earth.x,earth.y)
                        asteroidArr.append(asteroi)

                    totalEnemy = waveCount*2    
                    waveCount += 1  
                    countdownStart = False

                else:
                    for i in range(waveCount*3):

                        astroId = random.randint(1,2)#COUNTDOWN
                        if astroId == 1:

                            asteroi = Asteroid(10,10,50,50, alien_images)#ASTEROID ID
                            asteroi.id=astroId

                        else:

                            asteroi = spawnRandomSt(astroId)

                        asteroi.calcDist(earth.x,earth.y)
                        asteroidArr.append(asteroi)

                    totalEnemy = waveCount*3    
                    waveCount += 1  
                    countdownStart = False
            

            try:
                for i in range(len(asteroidArr)) : 
                    if asteroidArr[i].id == 1:
                        asteroidArr[i].moveFibo(earth.x,earth.y)# ASTEROID PLACE /MOVEMENT
                    elif asteroidArr[i].id == 3 and frameCounter % 60 == 0:
                        asteroidArr[i].blip()
                        
                        

                    elif asteroidArr[i].id == 2:
                        asteroidArr[i].moveStraight(earth.x,earth.y)

                    if asteroidArr[i].body.colliderect(earth.body):
                        if asteroidArr[i].name == "decebal" or asteroidArr[i].name == "cesar":
                            heartVal-=0.1
                        else:
                            if HasShield:
                                heartVal -= 1.0
                                asteroidArr.pop(i)
                            else:
                                heartVal -= 2.0
                                asteroidArr.pop(i)


                    asteroidArr[i].update()
                    asteroidArr[i].draw(screen,(255,0,0))

                    if asteroidArr[i].image_index ==59:
                        asteroidArr.pop(i)

                    if asteroidArr[i].body.colliderect(earth.body) and waveCount!=10 and waveCount !=5 :
                        if asteroidArr[i].name == "decebal":
                            heartVal-=0.1
                            asteroidArr.pop(i)
                            
                        elif asteroidArr[i].name == "cesar":
                            heartVal -=0.1
                            if HasShield:
                                heartVal -= 1.0
                                asteroidArr.pop(i)
                            else:
                                heartVal -= 2.0
                                asteroidArr.pop(i)
            except:
                pass

                


            try:
                if asteroi.name == "decebal" or asteroi.name == "cesar":
                    if asteroi.health!=0:
                        health_text = font1.render(f"{asteroi.health}", True, (255,255,255))  # Text, anti-aliasing, color
                        flipped_text = pygame.transform.flip(health_text, False, True)
                        screen.blit(flipped_text, (asteroi.asteroidx-15,asteroi.asteroidy-80))
            except:
                pass 

                    

            try:
                for i in range(len(projArr)):
                    projArr[i].draw(screen,(255,0,0),asteroidArr,i)
                    projArr[i].update()
            except:
                pass

            try:
                for i in range(len(coinArr)):

                    if coinArr[i].body.colliderect(player.rotated_rect):
                            coinArr.pop(i)
                            coins+=10
                            coin_effect.play()
                    if coinArr[i].body.colliderect(player2.rotated_rect):
                            coinArr.pop(i)
                            coins+=10
                            coin_effect.play()


                    if isHole == True:
                        if coinArr[i].body.colliderect(blk.body):
                            coinArr.pop(i)


                        coinArr[i].attract(blk.x-35,blk.y-35)
                        
                    coinArr[i].draw(screen,(0,255,0)) 
                    coinArr[i].update()
            except Exception as f:
                print(f)

            if  frameCounter % 500 == 0 and isHole == False and waveCount != 10:#BLACK HOLE
                isHole = True
                blk = spawnRandomBH()

            if isHole == True:

                blk.draw(screen,(0,100,100))
                blk.update()
                if frameCounter % 1000 == 0:
                    isHole = False



            

            if len(asteroidArr)==0:
                kkk = f"WAVE {str(waveCount-1)} COMPLETE"
            else:
                kkk = f"WAVE {str(waveCount-1)}"

            score_text = font.render(kkk, True, (255,255,255))  # Text, anti-aliasing, color
            flipped_text = pygame.transform.flip(score_text, False, True)

            # Calculate the position for the flipped text

            # Blit the flipped text onto the screen
            screen.blit(flipped_text, (20,550))


            


            screen.blit(Border,(0,0))

            Heart.draw(screen, 20,20, 200)

            heart_text = font1.render(f"{int(heartVal)}%", True, (255,255,255))  # Text, anti-aliasing, color
            flipped_text = pygame.transform.flip(heart_text, False, True)
            screen.blit(flipped_text, (20,20))

            Coin.draw(screen, 550,535, 255)

            coin_text = font.render(f"{coins}$", True, (255,255,255))  # Text, anti-aliasing, color
            flipped_text = pygame.transform.flip(coin_text, False, True)
            screen.blit(flipped_text, (605,550))

            if CloseMainButton.draw(screen, 255, 100, 30,20, 0.05):
                if show_screen ==1:
                    pygame.quit()
                    try:
                        pygame.mixer.music.stop()
                    except:
                        pass
                
                    sys.exit()

            if Shop.draw(screen, 20, 20):
                show_screen=2
            

            if show_screen == 3:
                screen.blit(InfoGUI,(0,0))
                if CloseButton.draw(screen, 255, 100, 30,20, 0.05):
                    show_screen = 1

            

            if show_screen == 2:
                screen.blit(ShopGUI,(0,0))
                if CloseButton.draw(screen, 255, 100, 30,20, 0.05):
                    show_screen = 1

                Minigun.draw(screen, 85,260, 255)
                Protection.draw(screen, 85,85, 255)
                Bullet.draw(screen, 425,260, 255)
                Lup.draw(screen, 425,85, 255)

                if not HasMinigun:
                    if Buy1Button.draw(screen, 200, 100, 0,0, 0.05):
                        if coins >= 300:
                            HasMinigun = True
                            coins -= 300
                else:
                    screen.blit(Check,(300,320))
                if not HasShield:
                    if Buy2Button.draw(screen, 200, 100, 0,0, 0.05):
                        if coins >= 150:
                            HasShield = True
                            coins -= 150
                else:
                    screen.blit(Check,(300,125))
                if not HasBullet:
                    if Buy3Button.draw(screen, 200, 100, 0,0, 0.05):
                        if coins >= 200:
                            HasBullet = True
                            coins -= 200
                else:
                    screen.blit(Check,(640,320))
                if not HasWolf:
                    if Buy4Button.draw(screen, 200, 100, 0,0, 0.05):
                        if coins >= 1000:
                            HasWolf = True
                            coins -= 1000
                else:
                    screen.blit(Check,(640,125))

        if HasWolf or defeatDecebal == True:
            screen.blit(WinGUI, (0,0))

        if heartVal<0:
            screen.blit(LoseGUI,(0,0))
            

        if fade_in:
            # Increase alpha value gradually
            if logoAlpha < 320:
                screen.fill((255,255,255))
                logoAlpha += 5
                logoim.set_alpha(logoAlpha)
                screen.blit(logoim, logoim_rect)
            else:
                fade_in = False
                screen.fill((255,255,255))
                screen.blit(logoim, logoim_rect)

        else:
            if logoAlpha > 0:
                screen.fill((255,255,255))
                logoAlpha -= 10
                logoim.set_alpha(logoAlpha)
                screen.blit(logoim, logoim_rect)
            else:
                pass

            

            


        
        
        




        frameCounter +=1
        pygame.time.Clock().tick(60)

        final_screen.render(screen)
        image = Image.frombytes("RGBA", final_screen.window_size, final_screen.output.read())
        tk_image = ImageTk.PhotoImage(image)
        cnv.itemconfig(img, image=tk_image)
        root.update()
        



            


    
root = tk.Tk()
root.geometry(f"{screen_width}x{screen_height}")
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "#292438")
label = tk.Label(root)
label.place(relx=0.5, rely=0.5, anchor="center")
cnv = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
cnv.pack()
img = cnv.create_image(0,0,image=None, anchor="nw")

hwnd = pygame.display.get_wm_info()["window"]

# Embed the Pygame window into the Tkinter window
win32gui.SetParent(hwnd, label.winfo_id())
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)

# Schedule the update function to be called
root.after(1, update_game)
cnv.bind("<Motion>", on_mouse_motion)



center_window(root, screen_width, screen_height)
root.mainloop()
