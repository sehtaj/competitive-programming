# solve: List[List[str]] -> None

# Time Complexity: O(m * n), where m and n are the number of rows and columns
# Space Complexity: O(m * n) in worst case due to recursion/stack

def traverse(i, j, board, rows, cols, directions):
    stack = [(i, j)]
    while stack:
        currI, currJ = stack.pop()
        if board[currI][currJ] != 'O':
            continue

        board[currI][currJ] = 'T'

        for direction in directions:
            nextI = currI + direction[0]
            nextJ = currJ + direction[1]
            if 0 <= nextI < rows and 0 <= nextJ < cols and board[nextI][nextJ] == 'O':
                stack.append((nextI, nextJ))

def solve(board):
    if not board:
        return

    rows = len(board)
    cols =  len(board[0])
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

    for i in range(rows):
        if board[i][0] == 'O':
            traverse(i, 0, board, rows, cols, directions)
        if board[i][cols - 1] == 'O':
            traverse(i, cols - 1, board, rows, cols, directions)

    for j in range(cols):
        if board[0][j] == 'O':
            traverse(0, j, board, rows, cols, directions)
        if board[rows - 1][j] == 'O':
            traverse(rows - 1, j, board, rows, cols, directions)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'

#edge cases
# 1. Empty Board
# board = []
# solve(board)
# print(board)  # Output: []

# 2. All X
# board = [["X", "X"], ["X", "X"]]
# solve(board)
# print(board)  # Should remain unchanged

# 3. All O (all connected to border)
# board = [["O", "O"], ["O", "O"]]
# solve(board)
# print(board)  # Should remain unchanged

# 4. Surrounded Center O
# board = [["X", "X", "X", "X"],
#          ["X", "O", "O", "X"],
#          ["X", "X", "O", "X"],
#          ["X", "O", "X", "X"]]
# solve(board)
# print(board)
# Expected: [['X', 'X', 'X', 'X'],
#            ['X', 'X', 'X', 'X'],
#            ['X', 'X', 'X', 'X'],
#            ['X', 'O', 'X', 'X']]

# 5. Single Row
# board = [["O", "X", "O", "X"]]
# solve(board)
# print(board)  # Should remain unchanged since all O's are on border

# 6. Single Column
# board = [["O"], ["X"], ["O"], ["X"]]
# solve(board)
# print(board)  # Should remain unchanged since all O's are on border
