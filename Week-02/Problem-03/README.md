# Maximum Path Sum Between Any Two Nodes in a Binary Tree

## Problem Statement

Given a binary tree where each node contains an integer value, find the **maximum path sum** between any two nodes.

- The path must go through at least **one node**.
- The path **does not need to pass through the root**.
- A path is a sequence of nodes connected by edges; each node appears only once.

### Example

Input:
-10
/
9 20
/
15 7

Output: 42

Explanation: The path is 15 → 20 → 7, sum = 42.


---

## Approach / Solution

This problem can be solved using **post-order traversal** (bottom-up):

1. For each node, compute the maximum path sum including **either left or right child**, ignoring negative paths (treat negatives as 0).  
2. Calculate the **current path sum** including **both left and right children + current node**.  
3. Keep a **global variable** to store the maximum path sum found so far.  
4. Return the maximum path sum that includes the current node and **one subtree** to propagate to the parent.

**Algorithm Steps:**

1. Initialize `max_sum` as negative infinity.
2. Define a helper function that recursively computes:
   - `left = max(helper(node.left), 0)`
   - `right = max(helper(node.right), 0)`
   - `current = node.val + left + right`
   - Update `max_sum = max(max_sum, current)`
   - Return `node.val + max(left, right)` for parent's computation.
3. Call helper on the root node and return `max_sum`.

---

## Time and Space Complexity

- **Time Complexity:** `O(N)` – each node is visited once.  
- **Space Complexity:** `O(H)` – recursion stack where `H` is the height of the tree.  

---

## References

- [LeetCode – Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [GeeksforGeeks – Maximum Path Sum in Binary Tree](https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/)
- YouTube tutorials on Binary Tree Maximum Path Sum
