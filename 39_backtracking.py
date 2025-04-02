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
def generate_subsets(arr):   # Define the function that takes an array 'arr' as input
    """
    Generates all subsets of the array.
    
    - Uses backtracking to explore all combinations.
    - Time Complexity: O(2^n), Space Complexity: O(n) for recursion stack.
    - Recursive backtracking is beginner-friendly for combinatorial problems.
    """
    result = []   # Initialize an empty list to store all subsets
    def backtrack(start, path):   # Define a helper function with 'start' index and current 'path'
        result.append(path[:])    # Add a copy of the current path (subset) to the result
        for i in range(start, len(arr)):   # Loop through elements from 'start' to end of array
            path.append(arr[i])            # Include the current element in the subset
            backtrack(i + 1, path)         # Recurse with the next index to explore further
            path.pop()                     # Backtrack by removing the last element to try without it
    backtrack(0, [])   # Start backtracking from index 0 with an empty path
    return result      # Return the complete list of subsets

# Test the function
# print(generate_subsets([1, 2]))  # Output: [[], [2], [1], [1, 2]]


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
def permute_string(s):   # Define the function that takes a string 's' as input
    """
    Generates all permutations of the string.
    
    - Uses backtracking with swapping to generate permutations.
    - Time Complexity: O(n!), Space Complexity: O(n).
    - In-place swapping simplifies understanding.
    """
    result = []   # Initialize an empty list to store all permutations
    def backtrack(start):   # Define a helper function with 'start' as the current position
        if start == len(s):   # If we've placed all characters (reached the end)
            result.append(''.join(s))   # Add the current permutation to the result
        for i in range(start, len(s)):   # Loop through characters from 'start' to end
            s[start], s[i] = s[i], s[start]   # Swap current position with character at 'i'
            backtrack(start + 1)              # Recurse to fix the next position
            s[start], s[i] = s[i], s[start]   # Backtrack by swapping back to original state
    s = list(s)   # Convert string to a list for mutable operations (swapping)
    backtrack(0)  # Start backtracking from position 0
    return result # Return the list of all permutations

# Test the function
# print(permute_string("ab"))  # Output: ['ab', 'ba']


# ----------------------------------------------------------------------------------
# 3. Combination Sum (Simple)
"""
Task: Find all unique combinations of numbers from the array that sum to the target, allowing reuse of elements.
Example: [1, 2], target 4 → [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
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
# print(combination_sum([1, 2], 4))  # Output: [[1, 1, 1, 1], [1, 1, 2], [2, 2]]


# Solution
def combination_sum(arr, target):   # Define the function with array 'arr' and 'target' sum
    """
    Finds combinations of numbers that sum to the target (repetition allowed).
    
    - Uses backtracking to explore combinations.
    - Time Complexity: O(2^n) in worst case, Space Complexity: O(n).
    - Simple recursive approach is teachable.
    """
    result = []   # Initialize an empty list to store valid combinations
    def backtrack(start, path, current_sum):   # Helper function with 'start', 'path', and 'current_sum'
        if current_sum == target:   # If the current sum matches the target
            result.append(path[:])  # Add a copy of the current path to the result
            return                  # Stop this path as we found a valid combination
        if current_sum > target:    # If the current sum exceeds the target
            return                  # Stop exploring this path (pruning)
        for i in range(start, len(arr)):   # Loop through elements from 'start' to end
            path.append(arr[i])            # Include the current element in the combination
            backtrack(i, path, current_sum + arr[i])  # Recurse, allowing reuse of same element
            path.pop()                     # Backtrack by removing the last element
    backtrack(0, [], 0)   # Start backtracking from index 0, empty path, and sum 0
    return result         # Return the list of all valid combinations

# Test the function
# print(combination_sum([1, 2], 4))  # Output: [[1, 1, 1, 1], [1, 1, 2], [2, 2]]


# ----------------------------------------------------------------------------------
# 4. Solve 3x3 Maze
"""
Task: Find a path from the top-left to the bottom-right corner in a 3x3 grid, where 1 represents a path and 0 represents an obstacle. 
      Return the path as a list of coordinates if it exists, otherwise return None.
Example: [[1, 0, 1], [1, 1, 1], [0, 1, 1]] → Path exists → [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
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
def solve_maze(grid):   # Define the function that takes a 3x3 grid as input
    """
    Finds a path from (0,0) to (2,2) in a 3x3 grid (1 = path, 0 = obstacle).
    
    - Uses backtracking to explore possible paths.
    - Time Complexity: O(2^n) in worst case, Space Complexity: O(n).
    - Simple recursive exploration is beginner-friendly.
    """
    def is_valid(row, col):   # Helper function to check if a cell is valid
        return 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == 1   # Check bounds and if path (1)
    def backtrack(row, col, path):   # Helper function with current 'row', 'col', and 'path'
        if row == 2 and col == 2:    # If we've reached the target (bottom-right corner)
            path.append((2, 2))      # Add the end cell to the path
            return path              # Return the complete path
        if is_valid(row, col):       # If the current cell is valid (within bounds and a path)
            path.append((row, col))  # Add the current cell to the path
            if backtrack(row + 1, col, path):  # Try moving down
                return path                    # Return path if successful
            if backtrack(row, col + 1, path):  # Try moving right
                return path                    # Return path if successful
            path.pop()               # Backtrack by removing the last cell if no path found
        return None                  # Return None if no path is found from this position
    return backtrack(0, 0, [])       # Start backtracking from (0,0) with an empty path

# Test the function
grid = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
# print(solve_maze(grid))  # Output: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]


# ----------------------------------------------------------------------------------
# 5. N-Queens (Small N)
"""
Task: Place 4 queens on a 4x4 chessboard such that no two queens threaten each other. 
      Return all valid configurations as lists, where each list represents the column positions of queens in each row.
Example: [[1, 3, 0, 2], [2, 0, 3, 1]]
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
def solve_n_queens(n):   # Define the function that takes board size 'n' as input
    """
    Places n queens on an n x n board with no attacks.
    
    - Uses backtracking to try queen placements.
    - Time Complexity: O(n!), Space Complexity: O(n).
    - Simplified for small n, with clear safety checks.
    """
    def is_safe(board, row, col):   # Helper function to check if a queen can be placed
        for i in range(row):        # Check all previous rows
            if board[i] == col or abs(board[i] - col) == row - i:  # Same column or diagonal conflict
                return False         # Return False if there's a conflict
        return True                  # Return True if safe to place queen
    def backtrack(row):   # Helper function to place queens row by row
        if row == n:      # If all queens are placed (reached board size)
            result.append(board[:])  # Add a copy of the current configuration to the result
            return                   # Stop as we found a solution
        for col in range(n):   # Try placing a queen in each column of the current row
            if is_safe(board, row, col):  # If it's safe to place a queen here
                board[row] = col          # Place the queen in this column
                backtrack(row + 1)        # Recurse to place queen in the next row
                board[row] = -1           # Backtrack by resetting the position
    result = []   # Initialize an empty list to store all valid configurations
    board = [-1] * n   # Initialize board with -1 (no queens placed) for each row
    backtrack(0)       # Start backtracking from row 0
    return result      # Return all valid configurations

# Test the function
# print(solve_n_queens(4))  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]

