# 🎯 Problem of the Week – The 24 Game  
**Company:** Twitter | PayPal  
**Difficulty:** Hard  
**Topics:** Recursion, Backtracking, Expression Evaluation  

---

## 🧩 Scenario  
The **24 Game** is a classic puzzle: given four integers (1–9), determine if it’s possible to reach exactly **24** by inserting the operators `+`, `-`, `*`, `/` and grouping them with parentheses.  
This problem tests recursion, backtracking, and expression evaluation.

---

## 📜 Problem Statement  
Given a list of **4 integers**, check whether it’s possible to reach the value **24** using arithmetic operations and valid parentheses arrangements.  
Return **true** if possible, otherwise **false**.

---

## 📥 Input Format  
Four space-separated integers `a1 a2 a3 a4` (each between **1 and 9**).

## 📤 Output Format  
Print `true` if 24 can be formed, else `false`.

---

## 🧠 Examples  

**Input 1:**  
5 2 7 8

**Output 1:**  
true

**Explanation:** `(5 × 2 - 7) × 8 = 24`

---

**Explanation:** No combination of operations can produce 24.

---

## ⚙️ Approaches  

### 1. Brute Force Enumeration  
- Try all permutations of numbers.  
- Try all operator combinations.  
- Try all valid parenthesizations.  
- Time complexity is large but feasible (since N=4).  

### 2. Recursion & Backtracking (Efficient)  
- Pick any two numbers, apply an operation, and recurse with the reduced list.  
- Continue until one number remains.  
- Base case: check if it equals 24 (within a small floating-point margin).

---

⏱️ Complexity Analysis
Approach	                   Time Complexity	             Space Complexity
Brute Force Enumeration	       O(4! × 4^3) ≈ O(1536)	     O(4) recursion stack
Recursion & Backtracking	   Same (N=4) but practical	     O(4) recursion stack

## 🔗 Practice Links  
- [LeetCode 679 – 24 Game](https://leetcode.com/problems/24-game/)  
- [GeeksforGeeks – The 24 Game Problem](https://www.geeksforgeeks.org/the-24-game-problem/)
