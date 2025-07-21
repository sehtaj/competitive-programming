# islandsAndTreasure: List[List[int]] -> None (modifies grid in-place)

# Time Complexity: O(m * n), where m is rows and n is cols
# Space Complexity: O(m * n), for the BFS queue in the worst case

def bfs(grid, q, directions, rows, cols):
    while q:
        currI, currJ = q.pop(0)

        for direction in directions:
            nextI = currI + direction[0]
            nextJ = currJ + direction[1]

            if (
                0 <= nextI < rows and
                0 <= nextJ < cols and
                grid[nextI][nextJ] == 2147483647
            ):
                grid[nextI][nextJ] = grid[currI][currJ] + 1
                q.append((nextI, nextJ))

def islandsAndTreasure(grid) :
        if not grid:
            return

        rows = len(grid)
        cols = len(grid[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        q = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        bfs(grid, q, directions, rows, cols)

# edge cases
# 1. Empty grid
# grid = []
# Output: Nothing (function returns immediately)

# 2. All walls
# grid = [
#   [-1, -1],
#   [-1, -1]
# ]
# Output: No change (no gates to spread from)

# 3. All gates
# grid = [
#   [0, 0],
#   [0, 0]
# ]
# Output: No change (all already gates)

# 4. Mixed grid
# grid = [
#   [2147483647, -1, 0, 2147483647],
#   [2147483647, 2147483647, 2147483647, -1],
#   [2147483647, -1, 2147483647, -1],
#   [0, -1, 2147483647, 2147483647]
# ]
# Output:
# [
#   [3, -1, 0, 1],
#   [2, 2, 1, -1],
#   [1, -1, 2, -1],
#   [0, -1, 3, 4]
# ]

# 5. No gates
# grid = [
#   [2147483647, -1],
#   [-1, 2147483647]
# ]
# Output: No change
                    