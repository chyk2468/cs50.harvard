# CS50 AI Project 0b: Tic-Tac-Toe

An unbeatable automated Tic-Tac-Toe AI implemented using the **Minimax Algorithm** with **Alpha-Beta Pruning**, developed for Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

---

## 1. Overview & Problem Description

Tic-Tac-Toe is a classic two-player zero-sum game played on a $3 \times 3$ grid. Players alternate placing their marks (`X` and `O`). The first player to align three matching marks horizontally, vertically, or diagonally wins. If all nine squares are filled without a winner, the game ends in a tie.

The goal of this project is to implement an optimal adversarial search agent that **never loses**—either winning when the human opponent makes an error or forcing a draw under optimal human play.

---

## 2. Adversarial Search Formulation

- **State Space:** Board representation as a $3 \times 3$ grid containing `X`, `O`, or `EMPTY`.
- **Players:** `player(s)` returns whose turn it is (`X` always moves first).
- **Actions:** `actions(s)` returns all vacant `(row, col)` cells.
- **Transition Model:** `result(s, a)` returns a deep-copied next board state without mutating the original.
- **Terminal State:** `terminal(s)` evaluates whether three-in-a-row is achieved or all cells are filled.
- **Utility Function:** 
  $$\text{Utility}(s) = \begin{cases} +1 & \text{if } X \text{ wins} \\ -1 & \text{if } O \text{ wins} \\ 0 & \text{if draw} \end{cases}$$

### Minimax Algorithm with Alpha-Beta Pruning
Because Tic-Tac-Toe has a total of $3^9 = 19,683$ possible states (and at most 255,168 games), Minimax can explore the full game tree:
- **Maximizing Player ($X$):** Selects $\max_{a \in \text{Actions}(s)} \text{MinValue}(\text{Result}(s, a))$.
- **Minimizing Player ($O$):** Selects $\min_{a \in \text{Actions}(s)} \text{MaxValue}(\text{Result}(s, a))$.
- **Alpha-Beta Pruning:** Eliminates subtrees that cannot influence the final decision ($\alpha \ge \beta$), substantially accelerating move evaluation.

---

## 3. Project Structure

- `tictactoe.py`: Core game logic (`player`, `actions`, `result`, `winner`, `terminal`, `utility`, `minimax`, `max_value`, `min_value`).
- `runner.py`: Pygame graphical user interface allowing human vs. AI gameplay.
- `requirements.txt`: Python package requirements (`pygame`).
- `OpenSans-Regular.ttf`: Font asset used by the Pygame interface.

---

## 4. Execution Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the interactive game:**
   ```bash
   python runner.py
   ```

3. **Gameplay:**
   - Choose to play as `X` (first move) or `O` (second move).
   - Watch the Minimax AI calculate the optimal response in real time.

