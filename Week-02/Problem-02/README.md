# Misère Nim Game – First Player Forced Win

## Problem Statement

The game of **Misère Nim** is played on multiple heaps of stones. Two players take turns removing **one or more stones from exactly one heap**. The **player who removes the last stone loses** (misère variant).  

Given three non-zero heap sizes `[a, b, c]`, determine if the **first player** can force a win assuming optimal play.

### Input
- A list of three positive integers: `[a, b, c]` (each > 0).

### Output
- `True` if the first player has a forced win.
- `False` otherwise.

### Examples
| Input       | Output | Explanation                                       |
|------------|--------|--------------------------------------------------|
| [3, 4, 5]  | True   | First player can force a win.                   |
| [1, 1, 1]  | False  | First player loses with 3 heaps of size 1.     |
| [1, 1, 2]  | True   | First player can force a win with heap ≥ 2.    |

---

## Approach / Solution

The solution is based on the **theory of Misère Nim**:

1. **All heaps of size 1**  
   - First player wins if the number of heaps is **even**.  
   - First player loses if the number of heaps is **odd**.  
   - Reason: Each move removes one heap, and the last removal loses.  

2. **At least one heap ≥ 2**  
   - Play is like normal Nim:  
     - Compute the **nim-sum** (XOR of all heap sizes).  
     - If nim-sum ≠ 0 → first player can force a win.  
     - If nim-sum = 0 → first player loses.  

**Algorithm Steps:**

1. Let `a, b, c` be heap sizes.
2. If all heaps are 1 → return `False` (since 3 heaps is odd).  
3. Else:
   - Compute `xor_sum = a ^ b ^ c`.  
   - If `xor_sum != 0` → return `True`  
   - Else → return `False`  

---

## Time and Space Complexity

- **Time Complexity:** `O(1)` for 3 heaps (general case: `O(n)` for `n` heaps).  
- **Space Complexity:** `O(1)` (only storing heap values and xor sum).  

---

## References / Practice

- [LeetCode – Nim Game](https://leetcode.com/problems/nim-game/)  
- [GeeksforGeeks – Game of Nim](https://www.geeksforgeeks.org/nim-game/)  
- [YouTube – Nim Game Explanation](https://www.youtube.com/results?search_query=nim+game+explanation)
