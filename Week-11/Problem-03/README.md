# 📻 Problem of the Week – Minimum Radio Broadcast Range

**Company:** Spotify  
**Difficulty:** Medium  
**Topics:** Greedy, Binary Search, Arrays  

---

## 🧩 Problem Statement
You are given:
- A list of **listeners’ positions** along a 1D line.
- A list of **radio tower positions**.

Find the **minimum broadcast range (R)** such that **every listener** is within distance `R` of at least one tower.

---

### 💡 Example
**Input**
4
1 5 11 20
3
4 8 15


**Output**
5


**Explanation**
- Listener 1 → nearest tower 4 (distance 3)  
- Listener 5 → tower 4 or 8 (distance 1–3)  
- Listener 11 → tower 8 or 15 (distance 3–4)  
- Listener 20 → tower 15 (distance 5)  
👉 Minimum range required = **5**

---

## ⚙️ Approaches

### 1. Brute Force (O(N × M))
- For each listener, calculate distance to every tower.
- Take the **maximum of minimum distances**.
- Works but **too slow** for large inputs.

---

### 2. Binary Search (O(N log M))
- Sort tower positions.
- For each listener, use **binary search** to find the closest tower.
- Keep track of the **maximum closest distance** (that’s your range).

**Intuition:**  
Listeners farthest from any tower decide the minimum range required.

---

### 3. Two-Pointer Greedy (O(N + M))
- Sort both arrays.
- Move pointers to always find the nearest tower for each listener.
- Track maximum of these distances.

---

## ⏱️ Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Brute Force | O(N × M) | O(1) |
| Binary Search | O(N log M) | O(1) |
| Two-Pointer | O(N + M) | O(1) |

---


## 📚 References
- 🔗 [LeetCode 475 – Heaters](https://leetcode.com/problems/heaters/)
- 🔗 [GeeksforGeeks – Minimum Radius to Cover All Houses](https://www.geeksforgeeks.org/find-minimum-radius-of-heaters-to-cover-all-houses/)

---

👨‍💻 **Author:** Problem of the Week | Spotify Challenge
