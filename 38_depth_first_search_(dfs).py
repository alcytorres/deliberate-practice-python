# Depth First Search (DFS)


# 1. Preorder Traversal
"""
Task: Print nodes in preorder (root, left, right).
Example: [1, 2, 3] → [1, 2, 3]
Why: Basic recursive DFS practice.
"""

# Solution
def preorder_traversal(root):
    """
    Returns nodes in preorder (root, left, right).
    
    - Uses recursive DFS for simplicity.
    - Time Complexity: O(n), Space Complexity: O(h) where h is height.
    - Recursive approach is intuitive for tree traversal.
    """
    if not root:
        return []
    return ([root.val] + 
            preorder_traversal(root.left) + 
            preorder_traversal(root.right))

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(preorder_traversal(root))  # Output: [1, 2, 3]


# ----------------------------------------------------------------------------------
# 2. Count Leaf Nodes
"""
Task: Count the number of leaf nodes in a tree.
Example: [1, 2, 3] → 2 (2, 3)
Why: Reinforces recursion termination.
"""

# Solution
def count_leaves(root):
    """
    Counts the number of leaf nodes in the tree.
    
    - Uses recursive DFS to traverse and count leaves.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive solution is simple and beginner-friendly.
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1  # Leaf node
    return count_leaves(root.left) + count_leaves(root.right)

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(count_leaves(root))  # Output: 2


# ----------------------------------------------------------------------------------
# 3. Find All Root-to-Leaf Paths
"""
Task: List all paths from root to leaves.
Example: [1, 2, 3] → [[1, 2], [1, 3]]
Why: Builds path-tracking skills.
"""

# Solution
def all_paths(root):
    """
    Lists all paths from root to leaves.
    
    - Uses recursive DFS to build paths.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive path-building is clear and educational.
    """
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]  # Leaf node path
    left_paths = all_paths(root.left)
    right_paths = all_paths(root.right)
    return [[root.val] + path for path in left_paths + right_paths]

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(all_paths(root))  # Output: [[1, 2], [1, 3]]


# ----------------------------------------------------------------------------------
# 4. Check if Tree is Symmetric (Simple)
"""
Task: Check if a small tree is symmetric.
Example: [1, 2, 2] → True
Why: Direct prep for Symmetric Tree.
"""

# Solution
def is_symmetric(root):
    """
    Checks if a tree is symmetric around its root.
    
    - Uses recursive DFS with a helper to compare subtrees.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive mirroring is intuitive for symmetry.
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    return is_mirror(root, root) if root else True

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(2))
print(is_symmetric(root))  # Output: True


# ----------------------------------------------------------------------------------
# 5. Height of Tree
"""
Task: Compute the height of a binary tree.
Example: [1, 2, 3] → 2
Why: Uses DFS to explore depth.
"""

# Solution
def tree_height(root):
    """
    Computes the height of the binary tree.
    
    - Uses recursive DFS to find maximum depth.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive height calculation is standard and simple.
    """
    if not root:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(tree_height(root))  # Output: 2


