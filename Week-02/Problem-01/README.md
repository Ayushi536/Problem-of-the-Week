# Minimum Number of Perfect Squares

## 📌 Problem
Given a positive integer `n`, find the **minimum number of perfect squares** (like `1, 4, 9, 16...`) that sum up exactly to `n`.  
The same square can be used multiple times.

---

## 📝 Examples
- **Input:** `13` → **Output:** `2`  
  Explanation: `13 = 9 + 4`  

- **Input:** `27` → **Output:** `3`  
  Explanation: `27 = 9 + 9 + 9`  

- **Input:** `1` → **Output:** `1`  
  Explanation: `1 = 1²`  

---

## 💡 Approach (Dynamic Programming)

This problem is similar to the **coin change problem**:
- Coins = Perfect squares ≤ `n`
- Target = `n`

### Steps
1. Generate all perfect squares ≤ `n`.
2. Define `dp[i]` = minimum number of squares needed to sum to `i`.
3. Base case: `dp[0] = 0`.
4. Transition:  dp[i] = min(dp[i], dp[i - sq] + 1) for each square sq ≤ i
5. Final Answer = `dp[n]`.

🔎 Code Explanation

Perfect squares list: Precompute [1, 4, 9, ...] up to n.

DP array: dp[i] stores the minimum number of squares to sum to i.

Transition: For each i, try all squares ≤ i.
Update dp[i] = min(dp[i], 1 + dp[i - sq]).

Answer: dp[n].

⏱️ Complexity Analysis

Time Complexity:

Generating squares: O(√n)

Filling DP: O(n√n)

Total: O(n√n)

Space Complexity:

DP array: O(n)

Squares list: O(√n)

Total: O(n)
