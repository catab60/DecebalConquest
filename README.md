<p align="center">
  <img src="https://github.com/catab60/DecebalConquest/blob/main/poze/banner.gif?raw=true">
</p>

**Decebal Conquest** is a fast‑paced 48‑hour game jam project built for the iTEC 2024 Game Development sprint. You and a friend team up in local co‑op to fend off endless alien waves, defeat two fearsome bosses, and save Earth from destruction. Crafted entirely from scratch in Python with Pygame and OpenGL (plus a Tkinter trick for transparent CRT‑style borders), this jam-built shooter packs procedural surprises, voice-activated panic mode, and all the jam diversifiers you can handle.

---

## Jam Theme & Diversifiers

* **Theme:** Future
* **Diversifiers Implemented:**

  * **“I don’t know where I am”**, fully **procedural** level elements
  * **“Better with friends”**, local/online **multiplayer** co-op
  * **“Hot swap”**, switch weapons on the fly without menus
  * **“Simple to play”**, runs in your **browser via WebGL** on itch.io
  * **“Hoțomanii”**, AI thieves who **steal or destroy** your progress items
  * **“Decebal and Traian”**, nods to **Romanian history & myth**
  * **“What’s it for?”**, in-game **shops** to buy power-ups
  * **“Sixth Sense”**, **voice control**: scream to trigger panic mode & rapid fire

---

## Gameplay & Co-op

**Objective:**
Survive wave after wave of invaders and thieves, then face two legendary bosses, **Traian** and **Decebal**, to save Earth. Work with your friend to hold the line. If Earth’s health drops to 0% or Decebal reaches the planet, it’s game over.

---

## Keyboard Binds

* **Player 1 Movement:** `W`, `A`, `S`, `D`

* **Player 1 Shoot:** `E`

* **Player 2 Movement:** `Y`, `G`, `H`, `J`

* **Player 2 Shoot:** `U`

* **Next Wave:** `P` (only available once the current wave is cleared)

* **Weapon 1 (Default):** `1`

* **Minigun (Shop Item):** `2`

* **Special Voice Control:**
  Scream into your mic at any time to trigger **Panic Mode**. Both players’ fire rates skyrocket until your voice calms!

---

## Enemies & Bosses

* **Aliens**

  * Present every wave in increasing numbers
  * Two AI patterns:

    1. **Patrol Swarm**, fly in looping, synchronized patterns, forcing you to time shots
    2. **Hunter Drones**, lock onto a player for short bursts before dispersing
  * Weak individually, but deadly in groups

* **Spartans**

  * Spawn randomly between waves
  * Emit a magnetic pulse that pulls in all dropped coins and power-ups
  * Vanish immediately after siphoning resources. Must be eliminated quickly or you lose currency

* **Traian (First Boss)**

  * Teleports unpredictably around the arena edges
  * Fires **Massive Orbs** which, on impact, deal **double damage** to players and to Earth’s shield
  * Shields regenerate slowly if left unchallenged, so constant pressure is key

* **Decebal (Final Boss)**

  * Gradually advances toward Earth’s orbit, shrinking the safe battlefield
  * Has an enormous health pool. Every hit chips away, but he regenerates when idle
  * If he makes contact with the planet’s surface, you instantly lose
  * Defeat him before he lands to **win the game**

---

## Special Items & Shop

1. **Minigun**

   * Unlocks rapid-fire mode when you press `2`
2. **Explosive Ammo**

   * All shots deal **2× damage** in a small blast radius
3. **Earth Shield**

   * Adds an extra protective layer around Earth, boosting its max health
4. **“Lupul Dacic”**

   * Legendary artifact. Purchase this to auto-win if you can afford its steep cost

---

## Lives & Health

* **Players:** 10 lives each
* **Earth:** Starts at 100% health every run

---

## How to Run

### Prerequisites

* **Python 3.x**

### Getting Started

```bash
git clone https://github.com/yourusername/DecebalConquest.git
cd DecebalConquest
pip install -r requirements.txt
python main.py
```

> **Tip:** On Windows you may run the provided `main.exe` directly.

---

## About the Project

This fun, frantic shooter was a **massive learning experience**. We built a custom Pygame/OpenGL engine in just 48 hours, integrated procedural generation, AI thieves, voice control, WebGL export, and more. Every system, from physics to rendering to UI transparency via hidden Tkinter, was hand-crafted under the jam clock.

---

## Who We Are

Developed by:

* **Branc Andrei Cătălin** (me)
* **Bar Ayan**

Student developers proving you can make a full-blown shooter in two days, no fancy engine required!

<p align="center">
  <img src="https://github.com/catab60/DecebalConquest/blob/main/poze/1.jpg?raw=true" height="400">
  <img src="https://github.com/catab60/DecebalConquest/blob/main/poze/2.jpg?raw=true" height="400">
</p>

*Thank you for playing Decebal Conquest. Now load up, team up, and save the world!*
