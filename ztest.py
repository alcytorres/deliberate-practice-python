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
print(solve_n_queens(4))  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]