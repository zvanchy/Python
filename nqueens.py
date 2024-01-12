def is_safe(board, row, col, N):
    # Check if the queen can be placed at board[row][col]
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed, add the current solution
    if col >= N:
        solution = []
        for i in range(N):
            solution.append(list(board[i]))
        solutions.append(solution)
        return

    # Consider this column and try placing a queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_queens_util(board, col + 1, N, solutions)

            # Backtrack and reset the cell when returning
            board[i][col] = 0


def solve_n_queens(N):
    # Create a N x N board initialized to 0
    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_queens_util(board, 0, N, solutions)

    return solutions


# Example: Get all solutions for 4 queens
all_solutions = solve_n_queens(4)
for solution in all_solutions:
    for row in solution:
        print(row)
    print()
