# CS50 AI Project 1b: Minesweeper

An automated propositional logic and knowledge-based Minesweeper player implemented for Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

---

## 1. Overview & Problem Description

Minesweeper is a puzzle game set on a grid of cells with randomly distributed hidden mines. The goal is to uncover all safe cells without detonating any mine.

When a player clicks a safe cell, the game reveals the number of neighboring cells (horizontally, vertically, and diagonally adjacent) that contain mines. The AI uses these numerical clues to logically deduce the locations of hidden mines and identify guaranteed safe moves.

---

## 2. Knowledge Representation & Inference

### The `Sentence` Class
Knowledge is represented using logical sentences of the form:
$$\{\text{cell}_1, \text{cell}_2, \dots, \text{cell}_k\} = \text{count}$$
This asserts that exactly $\text{count}$ of the given cells contain mines.

Key inference rules:
1. **Known Mines**: If $\text{len}(\text{cells}) == \text{count}$ and $\text{count} > 0$, then every cell in the sentence is guaranteed to be a mine.
2. **Known Safes**: If $\text{count} == 0$, then every cell in the sentence is guaranteed to be safe.
3. **Subset Inference**: If sentence $S_1$ is a subset of sentence $S_2$:
   $$S_1 = \{\text{cells}_1\} = \text{count}_1$$
   $$S_2 = \{\text{cells}_2\} = \text{count}_2$$
   where $\text{cells}_1 \subseteq \text{cells}_2$, then we can infer a new sentence:
   $$\text{cells}_2 - \text{cells}_1 = \text{count}_2 - \text{count}_1$$

### The `MinesweeperAI` Class
The AI agent tracks:
- `moves_made`: Cells that have already been played.
- `mines`: Cells proven to be mines.
- `safes`: Cells proven to be safe.
- `knowledge`: List of active `Sentence` objects.

When a cell is revealed with a count of neighboring mines, `add_knowledge` updates the agent's knowledge and iteratively infers new safe cells, mines, and subset relations until reaching a fixpoint (no further deductions possible).

---

## 3. Running the Project

### Requirements
The graphical interface requires `pygame`. To install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Running the Graphical Game

```bash
python runner.py
```

- Click **Play Game** to begin.
- Click **AI Move** to allow the agent to deduce and execute the next optimal move.
- The AI will always choose guaranteed safe moves whenever available, and falls back to an unrevealed, non-mine random move only when forced to make a probabilistic guess.
- Click **Reset** to start a new board.
