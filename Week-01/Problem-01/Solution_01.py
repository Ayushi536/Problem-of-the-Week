class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    
    # Step 1: Clone nodes and store mapping in a dictionary
    node_map = {}
    current = head
    while current:
        node_map[current] = Node(current.val)
        current = current.next
    
    # Step 2: Assign next and random pointers using the map
    current = head
    while current:
        node_map[current].next = node_map.get(current.next)
        node_map[current].random = node_map.get(current.random)
        current = current.next
    
    return node_map[head]

# Example usage:
# Node setup as per example
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

cloned_head = copyRandomList(node1)
