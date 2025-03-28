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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
from collections import deque

def level_order_traversal(root):
    """
    Prints nodes of a binary tree level by level.
    
    - Uses a queue for BFS to process nodes level-wise.
    - Time Complexity: O(n), Space Complexity: O(w) where w is max width.
    - Queue-based BFS is standard and beginner-friendly.
    """
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


# ----------------------------------------------------------------------------------
# 2. Count Nodes at Level K
"""
Task: Count nodes at a given level in a tree.
Example: [1, 2, 3], k=1 → 2 (2, 3)
Why: Reinforces level tracking."
"""

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
def count_nodes_at_level(root, k):
    """
    Counts nodes at a given level k (root is level 0).
    
    - Uses BFS to reach the target level and count nodes.
    - Time Complexity: O(n), Space Complexity: O(w).
    - Straightforward BFS application.
    """
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


# ----------------------------------------------------------------------------------
# 3. Shortest Path in Grid
"""
Task: Find the shortest path from top-left to bottom-right in a 3x3 grid.
Example: [[1, 1, 1], [1, 0, 1], [1, 1, 1]] → 4
Why: Applies BFS to a simple graph.
"""

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
def shortest_path_in_grid(grid):
    """
    Finds shortest path from (0,0) to bottom-right in a grid (1 = path, 0 = obstacle).
    
    - Uses BFS for shortest path in an unweighted graph.
    - Time Complexity: O(rows * cols), Space Complexity: O(rows * cols).
    - BFS is optimal and beginner-friendly for shortest paths.
    """
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


# ----------------------------------------------------------------------------------
# 4. Check if Tree is Complete
"""
Task: Verify if a binary tree is complete (all levels filled except possibly the last).
Example: [1, 2, 3, 4] → True
Why: Uses BFS to check structure.
"""

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
def is_complete_tree(root):
    """
    Verifies if a binary tree is complete (all levels full except possibly last).
    
    - Uses BFS to detect gaps in node placement.
    - Time Complexity: O(n), Space Complexity: O(w).
    - BFS with null tracking is clear for completeness check.
    """
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


# ----------------------------------------------------------------------------------
# 5. Find Distance to Leaf
"""
Task: Find the distance from root to the nearest leaf.
Example: [1, 2, null, 3] → 2
Why: Prepares for depth-related problems."
"""

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
def min_distance_to_leaf(root):
    """
    Finds the minimum distance from root to any leaf.
    
    - Uses BFS to find the shortest path to a leaf.
    - Time Complexity: O(n), Space Complexity: O(w).
    - BFS ensures shortest path, suitable for beginners.
    """
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

