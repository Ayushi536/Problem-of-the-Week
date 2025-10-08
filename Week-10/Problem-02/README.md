# 🎯 Problem of the Week – Bitwise AND of a Range  

**Company:** Yahoo  
**Difficulty:** Medium  
**Topics:** Bit Manipulation  

---

## 📌 Problem Statement  
Write a function that returns the **bitwise AND** of all integers between `M` and `N` (inclusive).  

Formally:  
result = M & (M+1) & (M+2) & ... & N


---

## 📥 Input Format  
Two integers `M` and `N` (0 ≤ M ≤ N ≤ 10^9).

## 📤 Output Format  
A single integer representing the bitwise AND of all numbers in the range `[M, N]`.

---

## 🧠 Examples  

**Example 1:**  
**Input:**  
M = 5, N = 7

**Output:**  
4

**Explanation:**  
5 = 101
6 = 110
7 = 111
5 & 6 & 7 = 100 = 4

---

## ⚙️ Approaches  

### 1. Naive Approach  
- Iterate from `M` to `N`.  
- Continuously apply the `&` operator.  
- **Time Complexity:** O(N-M) → inefficient for large ranges.  

### 2. Optimized Approach (Bitwise Trick) ✅  
- Observation: the result is the **common prefix** of `M` and `N` in binary.  
- Steps:  
  1. Initialize a `shift` counter to 0.  
  2. While `M != N`:  
     - Right shift both `M` and `N` by 1.  
     - Increment `shift`.  
  3. Left shift `M` back by `shift` → this is the result.  
- **Time Complexity:** O(log N)  
- **Space Complexity:** O(1)  

---


⏱️ Complexity Analysis
Approach	            Time Complexity	    Space Complexity
Naive	                O(N-M)	            O(1)
Bitwise Prefix Trick	O(log N)	        O(1)
🔗 Practice Links

LeetCode – Bitwise AND of Numbers Range

GeeksforGeeks – Bitwise AND of a Range
