# Flood Fill Algorithm

## Problem Statement

Given a 2D image represented as a matrix of characters, perform a **flood fill** starting from a given pixel (sr, sc):

- Change the color of the starting pixel and all **connected pixels** with the same original color to a new color `C`.
- Pixels are connected **4-directionally** (up, down, left, right). Diagonals are not considered.

### Example

Input:
image = [
['B', 'B', 'W'],
['W', 'W', 'W'],
['W', 'W', 'W'],
['B', 'B', 'B']
]
sr = 2, sc = 2
C = 'G'

Output:
[
['B', 'B', 'G'],
['G', 'G', 'G'],
['G', 'G', 'G'],
['B', 'B', 'B']
]


Explanation: The pixel at (2, 2) is 'W'. All connected 'W' pixels are changed to 'G'.

---

## Approach / Solution

### 1. DFS (Depth First Search)

1. Record the original color of the starting pixel.
2. Recursively visit all 4-directionally connected pixels with the same color.
3. Update each visited pixel to the new color.
4. Stop recursion when the pixel is out of bounds or has a different color.

### 2. BFS (Breadth First Search) [Optional]

1. Use a queue to perform level-order traversal.
2. Start from the given pixel and enqueue all 4-directionally connected pixels with the same color.
3. Update the color as pixels are dequeued.

---

## Time and Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|----------------|
| DFS      | O(N*M)         | O(H) recursion stack (H = height of region) |
| BFS      | O(N*M)         | O(N*M) queue worst-case |

Where N = number of rows, M = number of columns.

---

## Constraints

- 1 ≤ rows, cols ≤ 100
- C is an uppercase character
- Original image contains only uppercase characters

---

## References / Practice

- [LeetCode – Flood Fill](https://leetcode.com/problems/flood-fill/)
- [GeeksforGeeks – Flood Fill Algorithm](https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/)
- YouTube – Flood Fill Algorithm (DFS & BFS)
