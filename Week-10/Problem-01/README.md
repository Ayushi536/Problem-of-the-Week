# 🎯 Problem of the Week – Knight’s Survival Probability  

**Company:** Two Sigma  
**Difficulty:** Medium / Hard  
**Topics:** Dynamic Programming, Probability, Recursion  

---

## 🧩 Scenario  
A knight on a chessboard moves with its usual L-shaped moves.  
If it moves off the board at any step, it disappears and cannot return.  
Given a starting position and number of moves `k`, compute the probability that the knight remains on the board after exactly `k` moves.  

This models a **random-walk survival probability** with absorbing (off-board) states.

---

## 📜 Problem Statement  
Given:  
- An **8×8 chessboard** (0-indexed rows and columns).  
- A starting square `(r, c)`.  
- An integer `k` (number of moves).  

At each move, the knight chooses **uniformly from all 8 possible moves**.  
If a move lands off the board, the knight disappears.  

Return the **probability** that the knight stays on the board after exactly `k` moves.

---

## 📥 Input Format  
Three integers `r c k` where `0 ≤ r, c ≤ 7` and `k ≥ 0`.

## 📤 Output Format  
A floating-point number `p` (0 ≤ p ≤ 1) representing the probability that the knight remains on-board after `k` moves.

---

## 🧠 Examples  

**Example 1:**  
**Input:**  
0 0 1

**Output:**  
0.25

**Explanation:** From corner `(0,0)` the knight has **2 legal moves out of 8**, probability = 2/8 = 0.25.

---

## ⚙️ Approaches  

### 1. Dynamic Programming (Bottom-Up) ✅  
- Let `dp[t][i][j]' = probability that the knight is at `(i,j)` after `t` moves and still on-board.  
- Initialize: `dp[0][r][c] = 1.0`  
- For each move `t` from `0` to `k-1`:  
  - For each cell `(i,j)`, distribute `dp[t][i][j] / 8` among all 8 knight moves that stay on-board.  
- Result: sum over all `dp[k][i][j]`.  
- **Optimization:** Use rolling arrays (`curr` and `next_dp`) to reduce space.

---

### 2. Recursion + Memoization (Top-Down)  
- Define `P(t, i, j)` = probability to remain on-board after `t` remaining moves starting from `(i,j)`  
- Base case: `P(0, i, j) = 1` if `(i,j)` on-board  
- Recurrence: `P(t, i, j) = (1/8) * sum(P(t-1, ni, nj) for each knight move (ni,nj))`  
- Memoize `(t, i, j)` to avoid recomputation.  

---

### 3. Matrix Exponentiation (Advanced)  
- Treat board as **64×64 transition matrix T**.  
- Probability vector after k moves = `v0 * T^k`.  
- Overkill for small 8×8 board but possible for larger generalized boards.  

---
⏱️ Complexity Analysis
Approach	              Time Complexity	         Space Complexity
Bottom-Up DP	          O(k * 64 * 8) ≈ O(k)	     O(64) (rolling arrays)
Recursion + Memoization	  O(k * 64 * 8) ≈ O(k)	     O(k * 64) memoization
Matrix Exponentiation	  O(log k * 64^3)	         O(64^2)
🔗 Practice Links

LeetCode 688 – Knight Probability in Chessboard