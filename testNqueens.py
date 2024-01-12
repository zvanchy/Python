def n_queens_problem(n):
    board = [[0]*n for _ in range(n)]
    solutions = []
    n_queens_problem_recursive(board, 0, n, solutions)

    for solution in solutions:
        for item in solution:
            print(item)
        print()


def _is_safe(board, row, col, n):

    # check the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # # check top and bottom
    # for j in range(row):
    #     if board[j][col] == 1:
    #         return False

    # check diagon top left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check diagonal bottom left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_queens_problem_recursive(board, col, n, solutions):
    if col >= n:
        solution = []
        for i in range(n):
            solution.append(list(board[i]))
        solutions.append(solution)
        return

    for i in range(n):
        if _is_safe(board, i, col, n):
            board[i][col] = 1
            n_queens_problem_recursive(board, col + 1, n, solutions)
            board[i][col] = 0


n = 4
n_queens_problem(n)
