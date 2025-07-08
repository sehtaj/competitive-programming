# isValidSudoku: List[List[str]] → bool

# Time Complexity: O(1)
# Space Complexity: O(1)


def isValidSudoku(board):
    for i in range(9):
        rowSet = set()
        colSet = set()
        boxSet = set()

        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])

            if board[j][i] != '.':
                if board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])

            square_row = 3 * (i // 3)
            square_col = 3 * (i % 3)
            row = square_row + j // 3
            col = square_col + j % 3
            if board[row][col] != '.':
                if board[row][col] in boxSet:
                    return False
                boxSet.add(board[row][col])

    return True

# isValidSudoku([["1","2",".",".","3",".",".",".","."],
#                ["4",".",".","5",".",".",".",".","."],
#                [".","9","1",".",".",".",".",".","3"],
#                ["5",".",".",".","6",".",".",".","4"],
#                [".",".",".","8",".","3",".",".","5"],
#                ["7",".",".",".","2",".",".",".","6"],
#                [".",".",".",".",".",".","2",".","."],
#                [".",".",".","4","1","9",".",".","8"],
#                [".",".",".",".","8",".",".","7","9"]])