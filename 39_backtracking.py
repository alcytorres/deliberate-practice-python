# Backtracking
"""
Foundational Skills
   - Recursion
   - Decision tree exploration
Potential Knowledge Gaps
   - Knowing when to backtrack
   - Managing state during recursion
"""

# ----------------------------------------------------------------------------------
# 1. Generate All Subsets
"""
Task: List all subsets of a small set.
Example: [1, 2] → [[], [2], [1], [1, 2]]
Why: Introduces choice exploration.
"""

def generate_subsets(arr):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Add current subset
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack by removing last element
    backtrack(0, [])
    return result

# Test the function
# print(generate_subsets([1, 2]))  # Output: [[], [1], [1, 2], [2]]


# Solution
def generate_subsets(arr):
    """
    Generates all subsets of the array.
    
    - Uses backtracking to explore all combinations.
    - Time Complexity: O(2^n), Space Complexity: O(n) for recursion stack.
    - Recursive backtracking is beginner-friendly for combinatorial problems.
    """
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Add current subset
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack by removing last element
    backtrack(0, [])
    return result

# Test the function
# print(generate_subsets([1, 2]))  # Output: [[], [1], [1, 2], [2]]


# ----------------------------------------------------------------------------------
# 2. Permutations of a String
"""
Task: Generate all permutations of a short string.
Example: "ab" → ["ab", "ba"]
Why: Core backtracking practice.
"""

def permute_string(s):
    result = []
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]  # Backtrack
    s = list(s)
    backtrack(0)
    return result

# Test the function
# print(permute_string("ab"))  # Output: ['ab', 'ba']


# Solution
def permute_string(s):
    """
    Generates all permutations of the string.
    
    - Uses backtracking with swapping to generate permutations.
    - Time Complexity: O(n!), Space Complexity: O(n).
    - In-place swapping simplifies understanding.
    """
    result = []
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]  # Backtrack
    s = list(s)
    backtrack(0)
    return result

# Test the function
# print(permute_string("ab"))  # Output: ['ab', 'ba']


# ----------------------------------------------------------------------------------
# 3. Combination Sum (Simple)
"""
Task: Find combinations of numbers summing to a target.
Example: [1, 2], target 3 → [[1, 2]]
Why: Teaches state management.
"""

def combination_sum(arr, target):
    result = []
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i, path, current_sum + arr[i])  # Allow reuse
            path.pop()
    backtrack(0, [], 0)
    return result

# Test the function
# print(combination_sum([1, 2], 3))  # Output: [[1, 2]]


# Solution
def combination_sum(arr, target):
    """
    Finds combinations of numbers that sum to the target (repetition allowed).
    
    - Uses backtracking to explore combinations.
    - Time Complexity: O(2^n) in worst case, Space Complexity: O(n).
    - Simple recursive approach is teachable.
    """
    result = []
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i, path, current_sum + arr[i])  # Allow reuse
            path.pop()
    backtrack(0, [], 0)
    return result

# Test the function
# print(combination_sum([1, 2], 3))  # Output: [[1, 2]]


# ----------------------------------------------------------------------------------
# 4. Solve 3x3 Maze
"""
Task: Find a path from start to end in a 3x3 grid.
Example: [[1, 0, 1], [1, 1, 1], [0, 1, 1]] → Path exists
Why: Applies backtracking to grids.
"""

def solve_maze(grid):
    def is_valid(row, col):
        return 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == 1
    def backtrack(row, col, path):
        if row == 2 and col == 2:
            path.append((2, 2))
            return path
        if is_valid(row, col):
            path.append((row, col))
            if backtrack(row + 1, col, path):  # Try down
                return path
            if backtrack(row, col + 1, path):  # Try right
                return path
            path.pop()
        return None
    return backtrack(0, 0, [])

# Test the function
grid = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
# print(solve_maze(grid))  # Output: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]


# Solution
def solve_maze(grid):
    """
    Finds a path from (0,0) to (2,2) in a 3x3 grid (1 = path, 0 = obstacle).
    
    - Uses backtracking to explore possible paths.
    - Time Complexity: O(2^n) in worst case, Space Complexity: O(n).
    - Simple recursive exploration is beginner-friendly.
    """
    def is_valid(row, col):
        return 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == 1
    def backtrack(row, col, path):
        if row == 2 and col == 2:
            path.append((2, 2))
            return path
        if is_valid(row, col):
            path.append((row, col))
            if backtrack(row + 1, col, path):  # Try down
                return path
            if backtrack(row, col + 1, path):  # Try right
                return path
            path.pop()
        return None
    return backtrack(0, 0, [])

# Test the function
grid = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
# print(solve_maze(grid))  # Output: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]


# ----------------------------------------------------------------------------------
# 5. N-Queens (Small N)
"""
Task: Place 4 queens on a 4x4 board so none attack each other.
Example: Output a valid configuration
Why: Classic backtracking problem.
"""

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False  # Check column and diagonals
        return True
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack
    result = []
    board = [-1] * n
    backtrack(0)
    return result

# Test the function
# print(solve_n_queens(4))  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]


# Solution
def solve_n_queens(n):
    """
    Places n queens on an n x n board with no attacks.
    
    - Uses backtracking to try queen placements.
    - Time Complexity: O(n!), Space Complexity: O(n).
    - Simplified for small n, with clear safety checks.
    """
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False  # Check column and diagonals
        return True
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack
    result = []
    board = [-1] * n
    backtrack(0)
    return result

# Test the function
# print(solve_n_queens(4))  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]

