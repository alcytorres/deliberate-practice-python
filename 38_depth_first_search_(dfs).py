# Depth First Search (DFS)
"""
Foundational Skills
   - Recursion
   - Stack (for iterative DFS)
Potential Knowledge Gaps
   - Managing recursion depth
   - Tracking visited nodes in graphs
"""

# ----------------------------------------------------------------------------------
# 1. Preorder Traversal
"""
Task: Print nodes in preorder (root, left, right).
Example: [1, 2, 3] → [1, 2, 3]
Why: Basic recursive DFS practice.
"""

def preorder_traversal(root):
    if not root:
        return []
    return ([root.val] + 
            preorder_traversal(root.left) + 
            preorder_traversal(root.right))

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(preorder_traversal(root))  # Output: [1, 2, 3]


# Solution
def preorder_traversal(root):   # Define the function that takes the root of a binary tree
    """
    Returns nodes in preorder (root, left, right).
    
    - Uses recursive DFS for simplicity.
    - Time Complexity: O(n), Space Complexity: O(h) where h is height.
    - Recursive approach is intuitive for tree traversal.
    """
    if not root:         # Check if the current node is None (base case)
        return []        # Return an empty list if there's nothing to process
    return ([root.val] +          # Start with the current node's value (root first)
            preorder_traversal(root.left) +   # Then add all values from the left subtree
            preorder_traversal(root.right))   # Finally add all values from the right subtree

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(preorder_traversal(root))  # Output: [1, 2, 3]


# ----------------------------------------------------------------------------------
# 2. Count Leaf Nodes
"""
Task: Count the number of leaf nodes in a tree.
Example: [1, 2, 3] → 2 (2, 3)
Why: Reinforces recursion termination.
"""

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1  # Leaf node
    return count_leaves(root.left) + count_leaves(root.right)

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(count_leaves(root))  # Output: 2


# Solution
def count_leaves(root):   # Define the function that takes the root of a binary tree
    """
    Counts the number of leaf nodes in the tree.
    
    - Uses recursive DFS to traverse and count leaves.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive solution is simple and beginner-friendly.
    """
    if not root:         # Check if the current node is None (base case)
        return 0         # Return 0 since there are no leaves here
    if not root.left and not root.right:  # Check if the node has no children
        return 1         # It's a leaf node, so count it as 1
    return (count_leaves(root.left) +    # Count leaves in the left subtree
            count_leaves(root.right))    # Add the count of leaves in the right subtree

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(count_leaves(root))  # Output: 2


# ----------------------------------------------------------------------------------
# 3. Find All Root-to-Leaf Paths
"""
Task: List all paths from root to leaves.
Example: [1, 2, 3] → [[1, 2], [1, 3]]
Why: Builds path-tracking skills.
"""

def all_paths(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [[root.val]]  # Leaf node path
    left_paths = all_paths(root.left)
    right_paths = all_paths(root.right)
    return [[root.val] + path for path in left_paths + right_paths]

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(all_paths(root))  # Output: [[1, 2], [1, 3]]


# Solution
def all_paths(root):   # Define the function that takes the root of a binary tree
    """
    Lists all paths from root to leaves.
    
    - Uses recursive DFS to build paths.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive path-building is clear and educational.
    """
    if not root:         # Check if the current node is None (base case)
        return []        # Return an empty list since there are no paths
    if not root.left and not root.right:  # Check if it's a leaf node
        return [[root.val]]  # Return a single path with just this node's value
    left_paths = all_paths(root.left)    # Get all paths from the left subtree
    right_paths = all_paths(root.right)  # Get all paths from the right subtree
    return [[root.val] + path            # Add the current node's value to the start of each path
            for path in left_paths + right_paths]  # Combine paths from both subtrees

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(all_paths(root))  # Output: [[1, 2], [1, 3]]


# ----------------------------------------------------------------------------------
# 4. Check if Tree is Symmetric (Simple)
"""
Task: Check if a small tree is symmetric.
Example: [1, 2, 2] → True
Why: Direct prep for Symmetric Tree.
"""

def is_symmetric(root):
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
# print(is_symmetric(root))  # Output: True


# Solution
def is_symmetric(root):   # Define the function that takes the root of a binary tree
    """
    Checks if a tree is symmetric around its root.
    
    - Uses recursive DFS with a helper to compare subtrees.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive mirroring is intuitive for symmetry.
    """
    def is_mirror(left, right):  # Helper function to compare two subtrees
        if not left and not right:  # If both nodes are None
            return True             # They match (symmetric)
        if not left or not right:   # If only one node is None
            return False            # They don’t match (not symmetric)
        return (left.val == right.val and        # Check if current node values are equal
                is_mirror(left.left, right.right) and  # Compare left’s left with right’s right
                is_mirror(left.right, right.left))     # Compare left’s right with right’s left
    return is_mirror(root, root) if root else True  # Start by comparing the tree with itself, or True if empty

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(2))
# print(is_symmetric(root))  # Output: True


# ----------------------------------------------------------------------------------
# 5. Height of Tree
"""
Task: Compute the height of a binary tree.
Example: [1, 2, 3] → 2
Why: Uses DFS to explore depth.
"""

def tree_height(root):
    if not root:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(tree_height(root))  # Output: 2


# Solution
def tree_height(root):   # Define the function that takes the root of a binary tree
    """
    Computes the height of the binary tree.
    
    - Uses recursive DFS to find maximum depth.
    - Time Complexity: O(n), Space Complexity: O(h).
    - Recursive height calculation is standard and simple.
    """
    if not root:         # Check if the current node is None (base case)
        return 0         # Return 0 since there’s no height here
    left_height = tree_height(root.left)    # Get the height of the left subtree
    right_height = tree_height(root.right)  # Get the height of the right subtree
    return 1 + max(left_height, right_height)  # Add 1 for the current node, take max of subtree heights

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(tree_height(root))  # Output: 2


