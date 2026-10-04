# CS50 AI Project 2b: Heredity

## Description
This project uses a Bayesian Network and inference by enumeration to assess the probability that individuals possess 0, 1, or 2 copies of a mutated gene (GJB2, which is associated with hearing impairment) and whether they exhibit the related physical trait, given observed evidence from family pedigree data.

---

## Algorithms & Probability Model
- **Unconditional Gene Probabilities:** For individuals with no parent data, baseline probabilities are assigned via `PROBS["gene"]`.
- **Mendelian Inheritance with Mutation:** For individuals with parents in the dataset, gene inheritance considers:
  - Probability of passing mutated gene:
    - 2 copies: $1 - \text{mutation}$ ($0.99$)
    - 1 copy: $0.5$
    - 0 copies: $\text{mutation}$ ($0.01$)
  - Child inheriting from mother and father independently.
- **Conditional Trait Expression:** $P(\text{trait} \mid \text{genes})$ mapped via `PROBS["trait"]`.
- **Inference by Enumeration:** Joint probability computed over all unobserved variables and normalized across gene and trait distributions.

---

## Python Requirements
- **Python Version:** 3.12 (compatible with Python 3.10+)
- **Dependencies:** Standard library only (`csv`, `itertools`, `sys`, `math`). No third-party packages required.

---

## How to Run the Program
Execute `heredity.py` from the project directory, passing the path to a family CSV file:

```bash
python heredity.py data/family0.csv
python heredity.py data/family1.csv
python heredity.py data/family2.csv
```

---

## Testing & Verification
Run the official CS50 verification tools (in CS50 Codespaces or Linux environment):

```bash
check50 ai50/projects/2024/x/heredity
style50 heredity.py
```
