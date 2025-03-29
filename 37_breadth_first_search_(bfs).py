# Breadth First Search (BFS)
"""
Foundational Skills
   - Graph/tree traversal
   - Queue data structure
Potential Knowledge Gaps
   - Unfamiliarity with queue operations
   - Tracking visited nodes or levels
"""

# TreeNode Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # Define a simple binary tree node
        self.val = val      # Value stored in the node
        self.left = left    # Left child (can be None)
        self.right = right  # Right child (can be None)
     
# ----------------------------------------------------------------------------------
# 1. Level Order Traversal (Simple Tree)
"""
Task: Print nodes of a binary tree level by level.
Example: [1, 2, 3] → [1], [2, 3]
Why: Core BFS practice for Maximum Depth of Binary Tree.
"""

from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # Process all nodes at current level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(level_order_traversal(root))  # Output: [[1], [2, 3]]


# Solution
from collections import deque   # Import deque for efficient queue operations

def level_order_traversal(root):   # Define the function that takes the root of a binary tree
    """
    Prints nodes of a binary tree level by level.
    
    - Uses a queue for BFS to process nodes level-wise.
    - Time Complexity: O(n), Space Complexity: O(w) where w is max width.
    - Queue-based BFS is standard and beginner-friendly.
    """
    if not root:         # Check if the tree is empty
        return []        # Return an empty list if there’s no root
    result = []          # Initialize a list to store the level order traversal
    queue = deque([root])  # Start the queue with the root node
    while queue:         # Continue until the queue is empty
        level = []       # Create a list to store nodes at the current level
        for _ in range(len(queue)):  # Process all nodes at the current level
            node = queue.popleft()   # Dequeue the front node
            level.append(node.val)   # Add its value to the current level list
            if node.left:            # If there’s a left child
                queue.append(node.left)  # Enqueue the left child
            if node.right:           # If there’s a right child
                queue.append(node.right) # Enqueue the right child
        result.append(level)     # Add the current level’s values to the result
    return result            # Return the list of lists representing level order traversal

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(level_order_traversal(root))  # Output: [[1], [2, 3]]


# ----------------------------------------------------------------------------------
# 2. Count Nodes at Level K
"""
Task: Count nodes at a given level in a tree.
Example: [1, 2, 3], k=1 → 2 (2, 3)
Why: Reinforces level tracking."
"""

from collections import deque   # Import deque for efficient queue operations

def count_nodes_at_level(root, k):
    if not root:
        return 0
    queue = deque([root])
    level = 0
    while queue:
        if level == k:
            return len(queue)  # Number of nodes at level k
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return 0

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(count_nodes_at_level(root, 1))  # Output: 2


# Solution
from collections import deque   # Import deque for efficient queue operations

def count_nodes_at_level(root, k):   # Define the function that takes the root and level 'k'
    """
    Counts nodes at a given level k (root is level 0).
    
    - Uses BFS to reach the target level and count nodes.
    - Time Complexity: O(n), Space Complexity: O(w).
    - Straightforward BFS application.
    """
    if not root:         # Check if the tree is empty
        return 0         # Return 0 since there are no nodes
    queue = deque([root])  # Start the queue with the root node
    level = 0            # Initialize the current level to 0
    while queue:         # Continue until the queue is empty
        if level == k:   # If we’ve reached the target level 'k'
            return len(queue)  # Return the number of nodes at this level
        for _ in range(len(queue)):  # Process all nodes at the current level
            node = queue.popleft()   # Dequeue the front node
            if node.left:            # If there’s a left child
                queue.append(node.left)  # Enqueue the left child
            if node.right:           # If there’s a right child
                queue.append(node.right) # Enqueue the right child
        level += 1       # Move to the next level
    return 0             # If the loop ends without finding level 'k', return 0

# Test the function
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print(count_nodes_at_level(root, 1))  # Output: 2


# ----------------------------------------------------------------------------------
# 3. Shortest Path in Grid
"""
Task: Find the shortest path from top-left to bottom-right in a 3x3 grid.
Example: [[1, 1, 1], [1, 0, 1], [1, 1, 1]] → 4
Why: Applies BFS to a simple graph.
"""

from collections import deque   # Import deque for efficient queue operations

def shortest_path_in_grid(grid):
    if not grid or grid[0][0] == 0:
        return -1
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        row, col, dist = queue.popleft()
        if row == rows - 1 and col == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] == 1 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

# Test the function
grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# print(shortest_path_in_grid(grid))  # Output: 4


# Solution
from collections import deque   # Import deque for efficient queue operations

def shortest_path_in_grid(grid):   # Define the function that takes a 2D grid
    """
    Finds shortest path from (0,0) to bottom-right in a grid (1 = path, 0 = obstacle).
    
    - Uses BFS for shortest path in an unweighted graph.
    - Time Complexity: O(rows * cols), Space Complexity: O(rows * cols).
    - BFS is optimal and beginner-friendly for shortest paths.
    """
    if not grid or grid[0][0] == 0:   # Check if grid is empty or start is blocked
        return -1                     # Return -1 since there’s no path
    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns
    queue = deque([(0, 0, 1)])     # Start from (0,0) with distance 1
    visited = {(0, 0)}             # Mark (0,0) as visited
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible moves: right, down, left, up
    while queue:                   # Continue until the queue is empty
        row, col, dist = queue.popleft()  # Dequeue the current position and distance
        if row == rows - 1 and col == cols - 1:  # If we’ve reached the bottom-right corner
            return dist              # Return the distance (shortest path length)
        for dr, dc in directions:    # Check all four possible directions
            nr, nc = row + dr, col + dc  # Calculate the new row and column
            if (0 <= nr < rows and 0 <= nc < cols and   # Check if the new position is within bounds
                grid[nr][nc] == 1 and (nr, nc) not in visited):  # And is a path and not visited
                visited.add((nr, nc))    # Mark the new position as visited
                queue.append((nr, nc, dist + 1))  # Enqueue with incremented distance
    return -1                      # If no path is found, return -1

# Test the function
grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# print(shortest_path_in_grid(grid))  # Output: 4


# ----------------------------------------------------------------------------------
# 4. Check if Tree is Complete
"""
Task: Verify if a binary tree is complete (all levels filled except possibly the last).
Example: [1, 2, 3, 4] → True
Why: Uses BFS to check structure.
"""

from collections import deque   # Import deque for efficient queue operations

def is_complete_tree(root):
    if not root:
        return True
    queue = deque([root])
    end = False  # Flag for when null nodes start appearing
    while queue:
        node = queue.popleft()
        if node is None:
            end = True
        else:
            if end:
                return False  # Non-null after null means not complete
            queue.append(node.left)
            queue.append(node.right)
    return True

# Test the function
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
# print(is_complete_tree(root))  # Output: True


# Solution
from collections import deque   # Import deque for efficient queue operations

def is_complete_tree(root):   # Define the function that takes the root of a binary tree
    """
    Verifies if a binary tree is complete (all levels full except possibly last).
    
    - Uses BFS to detect gaps in node placement.
    - Time Complexity: O(n), Space Complexity: O(w).
    - BFS with null tracking is clear for completeness check.
    """
    if not root:         # Check if the tree is empty
        return True      # An empty tree is complete
    queue = deque([root])  # Start the queue with the root node
    end = False          # Flag to indicate when we’ve seen a null node
    while queue:         # Continue until the queue is empty
        node = queue.popleft()  # Dequeue the front node
        if node is None:     # If the node is None
            end = True       # Set the flag to indicate we’ve seen a null
        else:                # If the node is not None
            if end:          # If we’ve already seen a null before this non-null node
                return False # Tree is not complete (gap found)
            queue.append(node.left)   # Enqueue left child (could be None)
            queue.append(node.right)  # Enqueue right child (could be None)
    return True          # If no gaps are found, the tree is complete

# Test the function
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
# print(is_complete_tree(root))  # Output: True


# ----------------------------------------------------------------------------------
# 5. Find Distance to Leaf
"""
Task: Find the distance from root to the nearest leaf.
Example: [1, 2, null, 3] → 2
Why: Prepares for depth-related problems."
"""

from collections import deque   # Import deque for efficient queue operations

def min_distance_to_leaf(root):
    if not root:
        return 0
    queue = deque([(root, 0)])  # (node, depth)
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth  # Leaf found
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return -1

# Test the function
root = TreeNode(1, TreeNode(2, TreeNode(3)))
# print(min_distance_to_leaf(root))  # Output: 2


# Solution
from collections import deque   # Import deque for efficient queue operations

def min_distance_to_leaf(root):   # Define the function that takes the root of a binary tree
    """
    Finds the minimum distance from root to any leaf.
    
    - Uses BFS to find the shortest path to a leaf.
    - Time Complexity: O(n), Space Complexity: O(w).
    - BFS ensures shortest path, suitable for beginners.
    """
    if not root:         # Check if the tree is empty
        return 0         # Return 0 since there are no leaves
    queue = deque([(root, 0)])  # Start the queue with the root and depth 0
    while queue:         # Continue until the queue is empty
        node, depth = queue.popleft()  # Dequeue the current node and its depth
        if not node.left and not node.right:  # If the node is a leaf (no children)
            return depth   # Return the depth of this leaf
        if node.left:      # If there’s a left child
            queue.append((node.left, depth + 1))  # Enqueue left child with incremented depth
        if node.right:     # If there’s a right child
            queue.append((node.right, depth + 1)) # Enqueue right child with incremented depth
    return -1            # If no leaf is found, return -1 (though this shouldn’t happen for a valid tree)

# Test the function
root = TreeNode(1, TreeNode(2, TreeNode(3)))
# print(min_distance_to_leaf(root))  # Output: 2

