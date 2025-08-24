# Find the Greatest Common Divisor (GCD) of N Numbers

## Problem Statement

Given `n` integers, compute their **Greatest Common Divisor (GCD)** — the largest number that divides all of them without leaving a remainder.

### Examples

**Example 1:**

Input:
3
42 56 14
Output:
14


Explanation:
- Factors of 42 → {1, 2, 3, 6, 7, 14, 21, 42}
- Factors of 56 → {1, 2, 4, 7, 8, 14, 28, 56}
- Factors of 14 → {1, 2, 7, 14}
- Greatest common factor = 14

**Example 2:**

Input:
4
8 16 32 64
Output:
8


---

## Approach / Solution

1. **Euclidean Algorithm** for two numbers:  
    gcd(a, b) = gcd(b, a % b)

2. Extend to `n` numbers by iteratively computing:
    result = arr[0]
    for i in 1 to n-1:
    result = gcd(result, arr[i])

3. Return the final `result`.

---

## Time and Space Complexity

| Metric             | Complexity |
|-------------------|------------|
| Time Complexity    | O(n log M) – n numbers, each gcd computation takes O(log M), where M is the largest number |
| Space Complexity   | O(1) – only storing the running GCD |

---

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^9

---

## References / Practice

- [LeetCode – Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)
- [GeeksforGeeks – GCD of N Numbers](https://www.geeksforgeeks.org/gcd-of-n-numbers-in-python/)
- Video: Euclidean Algorithm – GCD Explained
