# CS50 AI Project 1a: Knights

An automated propositional logic puzzle solver for the classic *Knights and Knaves* riddles from Raymond Smullyan, implemented for Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

---

## 1. Overview & Problem Description

On the mythical island of Knights and Knaves:
- **Knights** always tell the truth.
- **Knaves** always lie.
- Every inhabitant is either a knight or a knave, and nobody can be both.

Given spoken statements from one or more inhabitants, the goal is to determine the identity of each character using propositional logic and model checking.

### The Four Puzzles

1. **Puzzle 0**:
   - Inhabitant: A
   - Statement: A says *"I am both a knight and a knave."*
2. **Puzzle 1**:
   - Inhabitants: A, B
   - Statement: A says *"We are both knaves."* B says nothing.
3. **Puzzle 2**:
   - Inhabitants: A, B
   - Statements: A says *"We are the same kind."* B says *"We are of different kinds."*
4. **Puzzle 3**:
   - Inhabitants: A, B, C
   - Statements:
     - A says either *"I am a knight."* or *"I am a knave."*, but we do not know which.
     - B says *"A said 'I am a knave.'"*
     - B says *"C is a knave."*
     - C says *"A is a knight."*

---

## 2. Algorithm & Knowledge Representation

### Propositional Symbols
For each character $X \in \{A, B, C\}$:
- $X\text{Knight}$: "$X$ is a Knight"
- $X\text{Knave}$: "$X$ is a Knave"

### Game Rules (Axioms)
For every character:
1. **Exclusivity**: $\text{Or}(X\text{Knight}, X\text{Knave})$
2. **Mutual Exclusion**: $\text{Not}(\text{And}(X\text{Knight}, X\text{Knave}))$

### Character Statements
If character $X$ utters statement $S$:
$$\text{Biconditional}(X\text{Knight}, S)$$
Because knights tell the truth ($X\text{Knight} \implies S$) and knaves lie ($X\text{Knave} \implies \neg S$), the biconditional naturally captures both constraints.

### Model Checking
The inference engine in `logic.py` uses recursive model checking:
- It generates every possible truth assignment for the relevant propositional symbols.
- A query $\alpha$ is entailed by knowledge base $KB$ ($KB \models \alpha$) if and only if in every model where $KB$ is true, $\alpha$ is also true.

---

## 3. Running the Project

To execute the solver and display the deduced identities:

```bash
python puzzle.py
```

### Expected Output

```text
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```
