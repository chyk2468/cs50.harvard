# CS50 AI Project 2a: PageRank

## Project Overview
This project implements the PageRank algorithm used to rank the importance of web pages within a network. The implementation explores two fundamental approaches to compute PageRank:
1. **Random Surfer Model (Sampling):** Approximates PageRank by simulating a web surfer randomly traversing links according to a Markov chain.
2. **Iterative Algorithm:** Calculates exact PageRank values mathematically using a recursive convergence formula until equilibrium is reached.

---

## Background & Algorithms

### 1. The PageRank Concept
PageRank models web surfing as a directed graph where nodes represent HTML pages and edges represent hyperlinks. Pages that are linked to by many pages—or by highly-ranked pages—receive higher importance scores.

### 2. Damping Factor (`d = 0.85`)
A random surfer does not follow hyperlinks indefinitely. With probability `d` (0.85), the surfer randomly follows one of the links on the current page. With probability `1 - d` (0.15), the surfer jumps to a completely random page chosen uniformly across the entire corpus.

### 3. Transition Model (`transition_model`)
For any given page:
- Every page in the corpus receives a baseline random jump probability:
  $$\frac{1 - d}{N}$$
  where $N$ is the total number of pages in the corpus.
- If the page has outgoing links, each target page receives an additional probability:
  $$\frac{d}{|Links|}$$
- If a page has **no outgoing links** (dangling page), it is treated as having equal links to all pages in the corpus, assigning each page probability $\frac{1}{N}$.

### 4. Sampling Approach (`sample_pagerank`)
- Selects the first page uniformly at random from all pages in the corpus.
- Iteratively generates $n$ samples where each subsequent page is chosen according to the transition probability distribution of the previous page.
- Computes each page's PageRank as its visitation count divided by the total number of samples $n$.

### 5. Iterative Approach (`iterate_pagerank`)
- Initializes every page with an equal initial rank of $\frac{1}{N}$.
- Recursively updates PageRanks using the PageRank formula:
  $$PR(p) = \frac{1 - d}{N} + d \sum_{i \in LinksTo(p)} \frac{PR(i)}{NumLinks(i)}$$
- Dangling pages (pages with no outgoing links) distribute their rank equally across all $N$ pages.
- The iteration repeats until no page's rank changes by more than $0.001$ between consecutive steps.
- The final ranks are normalized so that their sum equals exactly $1$.

---

## Corpora Descriptions
- `corpus0/`: A simple 4-page test network exhibiting symmetric properties between `1.html` and `3.html`.
- `corpus1/`: A 7-page network representing search, games, and puzzle domains.
- `corpus2/`: An 8-page network containing a dangling page (`recursion.html`) with no outbound hyperlinks, testing the dangling-node redistribution logic.

---

## Installation & Requirements
- **Python Version:** 3.12 (compatible with Python 3.10+)
- **Dependencies:** Standard library only (`os`, `random`, `re`, `sys`, `math`). No third-party packages required.

---

## Execution Instructions
Run the script from within the `05-PageRank/` directory, specifying the target corpus directory:

```bash
python pagerank.py corpus0
python pagerank.py corpus1
python pagerank.py corpus2
```

---

## Testing & Verification
Verify consistency between sampling ($n = 10,000$) and iterative PageRank:
```bash
python pagerank.py corpus0
```
Expected output:
- Sampling estimates align within $\pm 0.02$ of iterative values.
- `2.html` receives the highest PageRank ($\approx 0.43$).
- `1.html` and `3.html` receive identical iterative scores ($\approx 0.22$) due to network symmetry.
- `4.html` receives the lowest rank ($\approx 0.13$).

