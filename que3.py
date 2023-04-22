def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check if there is a queen in the upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check if there is a queen in the lower left diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def backtrack(board, col):
        if col >= n:
            return True

        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1

                if backtrack(board, col+1):
                    return True

                board[row][col] = 0

        return False

    # Initialize an empty board
    board = [[0 for _ in range(n)] for _ in range(n)]

    if backtrack(board, 0):
        return board

    return None
# Example usage
n = 4
solution = solve_n_queens(n)

if solution is None:
    print("No solution exists.")
else:
    for row in solution:
        print(row)