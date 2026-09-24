# CS50 AI Project 0a: Degrees

An automated graph-search implementation to find the shortest degree of separation between any two actors using **Breadth-First Search (BFS)**, implemented for Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

---

## 1. Overview & Problem Description

According to the "Six Degrees of Kevin Bacon" game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

In this project, we generalize the problem to find the shortest path between **any two arbitrary actors** using data from IMDb.

---

## 2. Algorithm & Search Formulation

We model the problem as a graph search:
- **States:** Individual actors (`person_id`).
- **Actions:** Starring in a specific movie (`movie_id`).
- **Transitions:** Moving from one actor to a co-star via a shared movie.
- **Goal Test:** Whether the current state matches the target actor.
- **Path Cost:** Number of movies (each transition has equal cost = 1).

### Breadth-First Search (BFS)
Because all step costs are equal (1 degree per movie), **Breadth-First Search** is guaranteed to find the optimal (shortest) path. 
- Uses a **Queue-based Frontier** (`QueueFrontier` - FIFO).
- Tracks an `explored` set to avoid revisiting actors and prevent cycles.
- When expanding an actor node, all neighbors `(movie_id, person_id)` are extracted from the IMDb dataset and added to the frontier if not already visited or in the frontier.

---

## 3. Data Structure & Files

- `degrees.py`: Loads CSV data, prompts the user for two actors, runs BFS, and prints the resulting path.
- `util.py`: Data structures for search, including `Node`, `StackFrontier` (DFS), and `QueueFrontier` (BFS).
- `small/`: Small test dataset containing sample actors, movies, and stars.
- `large/`: Full IMDb dataset containing thousands of actors, movies, and relationships.

---

## 4. Execution Instructions

### Run with the small test dataset:
```bash
python degrees.py small
```

### Run with the full IMDb dataset:
```bash
python degrees.py large
```

### Example Output:
```text
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Robert De Niro starred in The Good Shepherd
3: Robert De Niro and Jennifer Lawrence starred in Silver Linings Playbook
```

---

## 5. Verification & Performance

- **Optimal Path Guarantee:** BFS explores all paths of length $k$ before any path of length $k + 1$.
- **Explored Set Optimization:** Using a hash set for explored actor IDs achieves $O(1)$ lookup time per node expansion.

