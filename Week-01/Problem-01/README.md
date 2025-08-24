# Deep Clone a Linked List with Random Pointer

## Problem Statement

Given a singly linked list where each node has two pointers:

- `next` → Points to the next node
- `random` → Points to any node in the list (or null)

Create a **deep copy** of the list where:

- Each node is a **new object**
- Values, `next`, and `random` pointers are identical
- Original and cloned lists are independent

### Example

Input:
Node1(val=7) → Node2(val=13) → Node3(val=11) → Node4(val=10) → Node5(val=1)
Random pointers:
Node2.random → Node1
Node3.random → Node5
Node4.random → Node3
Node5.random → Node1

Output: Deep cloned list with same values and pointer structure


---

## Approach

### 1. Hash Map Approach (O(n) space)

1. Traverse the original list and **create a new node for each original node**.
2. Store the mapping: `original_node → cloned_node` in a dictionary.
3. Traverse the original list again:
   - Assign `next` and `random` pointers of cloned nodes using the dictionary.

### 2. Optimized Interleaving Approach (O(1) space)

1. Interleave cloned nodes between original nodes.
Original: A → B → C
Interleaved: A → A' → B → B' → C → C'

2. Assign `random` pointers for cloned nodes using the interleaved structure.
3. Separate the cloned nodes from the original list.

---

## Time and Space Complexity

| Approach               | Time Complexity | Space Complexity |
|------------------------|----------------|----------------|
| Hash Map               | O(n)           | O(n)           |
| Interleaving (Optimized)| O(n)           | O(1)           |

---

## Verification

- Values of nodes are identical
- `next` and `random` pointers correspond correctly
- Original and cloned lists are **disconnected**

---

## References / Practice

- [LeetCode – Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [GeeksforGeeks – Clone Linked List with Random Pointer](https://www.geeksforgeeks.org/clone-linked-list-next-random-pointer-set-2/)
- YouTube: [NeetCode – Copy List with Random Pointer](https://www.youtube.com/watch?v=O9zjzQG9u7g)
