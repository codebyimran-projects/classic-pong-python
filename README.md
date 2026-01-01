
# Classic Pong Python

A classic **Pong game** built in **Python** using the Turtle graphics library.  
This project features a clean **start menu**, two-player local gameplay, score tracking, paddle movement, and a professional game loop.

---

## Game Features

- **Start Menu UI**
  - Press **P** to play
  - Press **Q** to quit
- **Two-player controls**
  - Player A: `W` (up), `S` (down)
  - Player B: `Up Arrow` (up), `Down Arrow` (down)
- Score tracking
- Collision detection (paddle + walls)
- Win condition (first to 10 points)
- Smooth gameplay and responsive controls

---

## Screenshots

*(Optional: add screenshots in this section if you like)*

---

## Controls

| Action | Key |
|--------|-----|
| Start Game | `P` |
| Quit Game | `Q` |
| Paddle A Up | `W` |
| Paddle A Down | `S` |
| Paddle B Up | `Up Arrow` |
| Paddle B Down | `Down Arrow` |

---

## Requirements

This project runs with:

- **Python 3.x**
- **Turtle Graphics** (pre-installed with Python)

No external dependencies are required.

---

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/codebyimran-projects/classic-pong-python.git
````

2. Navigate into the directory:

   ```bash
   cd classic-pong-python
   ```

3. Run the game:

   ```bash
   python main.py
   ```

4. Use the menu to **Play** or **Quit**.

---

## Project Structure

```
classic-pong-python/
│
├── main.py        # Main game program
└── README.md      # Project documentation
```

---

## How It Works

The game uses the **Turtle** library to:

* Draw paddles, ball, and score text
* Listen for keyboard events
* Update game state every frame
* Detect collisions and update scores

The game loop runs inside a `while True` block with `win.update()` driving animation.

---

## Author

**Imran**
GitHub: [https://github.com/codebyimran-projects](https://github.com/codebyimran-projects)

Created by **Code by Imran**
