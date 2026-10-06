# CS50 AI Project 3: Crossword Solver

## Description
This project implements an AI agent that generates crossword puzzles using Constraint Satisfaction Problem (CSP) algorithms and backtracking search. Given a grid structure and a vocabulary list, the solver determines words that fit each slot without character conflicts at intersections.

---

## Core Algorithms & CSP Formulation

### 1. Variables and Domains
- **Variables:** Each crossword slot is represented by a `Variable` object with a start coordinate `(i, j)`, direction (`ACROSS` or `DOWN`), and length.
- **Domains:** Initially, each variable's domain contains the entire set of vocabulary words.

### 2. Constraints
- **Unary (Node Consistency):** Every word in a variable's domain must match the variable's length.
- **Binary (Arc Consistency):** If two variables overlap at positions `(i, j)`, their assigned words must share the same letter at the intersection point.
- **Global:** All assigned words must be distinct across the entire crossword puzzle.

### 3. Inference & Heuristics
- **AC-3 Algorithm:** Enforces arc consistency across all directed pairs of overlapping variables, pruning values with no valid support.
- **Minimum Remaining Values (MRV):** Chooses the unassigned variable with the fewest remaining candidate values in its domain.
- **Degree Heuristic:** Breaks MRV ties by selecting the variable with the highest number of neighbors.
- **Least-Constraining Values (LCV):** Orders candidate domain values by the fewest conflicts ruled out for neighboring unassigned variables.
- **Backtracking Search:** Systematically explores partial assignments and backtracks upon reaching constraint dead ends.

---

## Requirements
- **Python Version:** 3.12 (compatible with Python 3.10+)
- **Dependencies:** Standard library only for solving (`sys`, `math`, `collections`). Optional `Pillow` for rendering crossword diagrams to image files.

---

## Execution
Run the solver by passing a crossword structure and wordlist:

```bash
python generate.py data/structure0.txt data/words0.txt
python generate.py data/structure1.txt data/words1.txt
python generate.py data/structure2.txt data/words2.txt
```

To render the solved puzzle to an image file:

```bash
python generate.py data/structure1.txt data/words1.txt output.png
```

---

## Testing & Verification
Run the official CS50 verification tools (in CS50 Codespaces or Linux environment):

```bash
check50 ai50/projects/2024/x/crossword
style50 generate.py
```
