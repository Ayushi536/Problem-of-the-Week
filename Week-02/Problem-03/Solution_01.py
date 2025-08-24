class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    """
    Compute the maximum path sum between any two nodes in a binary tree.

    Args:
    root (TreeNode): Root of the binary tree.

    Returns:
    int: Maximum path sum between any two nodes.
    """
    max_sum = float('-inf')  # Initialize global maximum

    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Recursively compute max path sum from left and right, ignore negatives
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        
        # Current max including both left and right paths through this node
        current = node.val + left + right
        
        # Update global maximum if current path sum is larger
        max_sum = max(max_sum, current)
        
        # Return max path sum including this node and one subtree (for parent usage)
        return node.val + max(left, right)
    
    helper(root)
    return max_sum


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxPathSum(root))  # Output: 42
