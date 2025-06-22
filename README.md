<p align="center">
  <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/banner.gif?raw=true">
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

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/alien.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Aliens</h2>
      <ul>
        <li>Present every wave in increasing numbers</li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/spartan.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Spartans</h2>
      <ul>
        <li>Spawn randomly between waves</li>
        <li>Emit a magnetic pulse that pulls in all dropped coins and power-ups</li>
        <li>Vanish immediately after siphoning resources. Must be eliminated quickly or you lose currency</li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/traian.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Traian (First Boss)</h2>
      <ul>
        <li>Teleports unpredictably around the arena edges</li>
        <li>Fires <strong>Massive Orbs</strong> which, on impact, deal <strong>double damage</strong> to players and to Earth’s shield</li>
        <li>Shields regenerate slowly if left unchallenged, so constant pressure is key</li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/decebal.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Decebal (Final Boss)</h2>
      <ul>
        <li>Gradually advances toward Earth’s orbit, shrinking the safe battlefield</li>
        <li>Has an enormous health pool. Every hit chips away, but he regenerates when idle</li>
        <li>If he makes contact with the planet’s surface, you instantly lose</li>
        <li>Defeat him before he lands to <strong>win the game</strong></li>
      </ul>
    </td>
  </tr>
</table>


---

## Special Items & Shop

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/minigun.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Minigun</h2>
      <ul>
        <li>Unlocks rapid-fire mode when you press <code>2</code></li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/ammo.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Explosive Ammo</h2>
      <ul>
        <li>All shots deal <strong>2× damage</strong> in a small blast radius</li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/shield.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>Earth Shield</h2>
      <ul>
        <li>Adds an extra protective layer around Earth, boosting its max health</li>
      </ul>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/lup.JPG?raw=true" width="200">
    </td>
    <td>
      <h2>“Lupul Dacic”</h2>
      <ul>
        <li>Legendary artifact. Purchase this to auto-win if you can afford its steep cost</li>
      </ul>
    </td>
  </tr>
</table>

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
git clone https://github.com/catab60/DecebalConquest.git
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
  <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/1.jpg?raw=true" height="400">
  <img src="https://github.com/catab60/DecebalConquest/blob/main/Decebal%20Conquest/poze/2.jpg?raw=true" height="400">
</p>

*Thank you for playing Decebal Conquest. Now load up, team up, and save the world!*
