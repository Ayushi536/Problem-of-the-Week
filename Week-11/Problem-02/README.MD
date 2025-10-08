# 🍏 Problem of the Week – Fixed Point in a Sorted Array

**Company:** Apple  
**Difficulty:** Medium  
**Topics:** Binary Search, Arrays  

---

## 🧩 Problem Statement
A **fixed point** in an array is an index `i` where:
> `arr[i] == i`

You are given a **sorted array of distinct integers**.  
Find and return any fixed point if it exists, otherwise return `False`.

---

### 🧠 Example

**Input**
4
-6 0 2 40


**Output**
2

✅ At index `2`, `arr[2] = 2`.

---

## ⚙️ Approach Breakdown

### 1. **Brute Force (O(N))**
- Iterate over every index `i`.
- Check if `arr[i] == i`.
- Return the index if found, else return `False`.

**Code Snippet:**
```python
for i in range(len(arr)):
    if arr[i] == i:
        return i
return False

2. Optimized Approach – Binary Search (O(log N))

Since the array is sorted and contains distinct elements:

Compare arr[mid] with mid.

If arr[mid] == mid → fixed point found.

If arr[mid] > mid → move left.

If arr[mid] < mid → move right.

This reduces search space by half each step.


⏱️ Time & Space Complexity
Approach	  Time Complexity	Space Complexity
Brute Force	    O(N)	           O(1)
Binary Search	O(log N)	       O(1)