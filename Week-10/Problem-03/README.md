# 🎯 Problem of the Week – Longest Increasing Subsequence (LIS)

**Company:** Microsoft  
**Difficulty:** Medium  
**Topic:** Dynamic Programming  

---

## 📌 Problem Statement  
Given an array of numbers, find the **length of the Longest Increasing Subsequence (LIS)**.  
The subsequence does **not need to be contiguous**, but the order must be maintained.

---

## 📥 Input Format  
- An array of integers `arr[]`.

## 📤 Output Format  
- An integer representing the length of the LIS.

---

## 🧠 Example  

**Input:**  
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

**Output:**  
6

**Explanation:**  
The LIS is `[0, 2, 6, 9, 11, 15]` with length 6.

---

## ⚙️ Approaches  

### 1. Recursive + Memoization (Top-Down DP)  
- Try including or excluding each element.  
- Memoize results to avoid recomputation.  
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n²) for memoization.

---

### 2. Bottom-Up DP (Classic DP) ✅  
- Maintain `dp[i]` = length of LIS ending at index `i`.  
- Transition:  
dp[i] = 1 + max(dp[j]) for all j < i where arr[j] < arr[i]

- Return `max(dp)` as the LIS length.  
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n)

---

### 3. Optimized Approach with Binary Search (Patience Sorting Method) ✅  
- Maintain a `temp` array representing smallest possible tail of increasing subsequences of different lengths.  
- For each number in the array:  
  - If greater than largest in `temp`, append it.  
  - Else, replace the smallest element ≥ current number.  
- Length of `temp` gives the LIS.  
- **Time Complexity:** O(n log n)  
- **Space Complexity:** O(n)

---

⏱️ Complexity Analysis
Approach	               Time Complexity	  Space Complexity
Recursive + Memoization	   O(n²)	          O(n²)
Bottom-Up DP	           O(n²)	          O(n)
Binary Search Optimized	   O(n log n)	      O(n)


🔗 Practice Links

LeetCode – Longest Increasing Subsequence
GeeksforGeeks – Longest Increasing Subsequence