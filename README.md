# ❌⭕ Tic Tac Toe – Minimax AI Player

This project implements a Tic Tac Toe game with an unbeatable AI using the Minimax algorithm. The AI can play as either X or O, and always makes the optimal move. The game features a graphical interface built with Pygame.

## 🧠 How It Works

The AI uses the **Minimax algorithm** with memoization to efficiently search the game tree and select the best possible move at every turn. The algorithm:

- Recursively simulates all possible moves and their outcomes.
- Assigns utility values to terminal states (+1 for X win, -1 for O win, 0 for tie).
- Chooses moves that maximize the AI's chance of winning (or minimize loss if playing as O).
- Uses memoization to avoid redundant calculations and speed up decision-making.

## 📂 Features

- Play as X or O against the AI.
- Graphical board rendered with Pygame.
- Displays game status and winner.
- "Play Again" button to restart the game.
- AI never loses!

## ▶️ Usage

To run the game, use:

python [runner.py]

## ⚙️ Requirements

- Python 3.7 or higher
- Pygame

## 💾 Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:noeEdwin/Tic-Tac-Toe.git
   cd tictactoe-minimax
   pip install pygame
