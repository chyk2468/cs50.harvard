# CS50 AI Project 4B: Nim Reinforcement Learning

## Author
`chyk2468`

## Overview
This project implements an AI agent that learns how to play the game of Nim using Reinforcement Learning (Q-learning). Through self-play over thousands of games, the agent optimizes its state-action value function $Q(s, a)$ to discover optimal moves and win consistently under Misère rules (the player who takes the last object loses).

---

## Game Rules (Nim - Misère)
- The game starts with four piles containing 1, 3, 5, and 7 objects respectively.
- On a player's turn, they must choose any non-empty pile and remove any positive number of objects from that pile.
- Under **Misère** rules, the player forced to take the final remaining object on the entire board **loses** the game (meaning the player who took the second-to-last object wins).

---

## Q-Learning Formulation

### 1. State Representation
- A game state $s$ is represented as a tuple of the remaining counts in each pile, e.g. `(1, 3, 5, 7)`.

### 2. Action Representation
- An action $a$ is represented as a tuple `(i, j)`, where $i$ is the pile index (0-indexed) and $j$ is the number of objects to remove from pile $i$ ($1 \le j \le \text{piles}[i]$).

### 3. Q-Value Update Formula
Whenever an agent takes action $a$ from state $s$, transitions to state $s'$, and receives immediate reward $r$, the Q-value is updated via:
$$Q(s, a) \leftarrow Q(s, a) + \alpha \Big(\big(r + \max_{a'} Q(s', a')\big) - Q(s, a)\Big)$$
where:
- $\alpha \in (0, 1]$ is the learning rate (`self.alpha = 0.5`).
- $r$ is the reward:
  - $+1$ for making a move that directly results in winning the game.
  - $-1$ for making a move that results in losing the game (taking the last object).
  - $0$ for all non-terminal moves.
- $\max_{a'} Q(s', a')$ is the estimated best future reward from the resulting state $s'$.

### 4. Action Selection ($\epsilon$-Greedy)
- With probability $\epsilon$ (`self.epsilon = 0.1` during training), the agent explores by picking a random available action from state $s$.
- With probability $1 - \epsilon$ (or when `epsilon=False`), the agent exploits known knowledge by choosing the action $a^*$ that maximizes $Q(s, a)$, breaking ties arbitrarily.

---

## Functions Implemented in `nim.py`
1. `get_q_value(self, state, action)`: Looks up and returns the stored Q-value in `self.q` for key `(tuple(state), action)`, or `0` if not yet encountered.
2. `update_q_value(self, state, action, old_q, reward, future_rewards)`: Updates `self.q[(tuple(state), action)]` using the standard Q-learning formula.
3. `best_future_reward(self, state)`: Finds and returns the maximum Q-value across all available actions for `state`. Returns `0` if no actions are available.
4. `choose_action(self, state, epsilon=True)`: Implements $\epsilon$-greedy action selection, picking a random available action with probability $\epsilon$, or the action with the maximum Q-value.

---

## Running the Project
Play against the trained AI:
```bash
python 09-Nim/play.py
```
Or from within the `09-Nim/` directory:
```bash
python play.py
```
