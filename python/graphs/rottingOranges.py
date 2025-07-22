# orangesRotting: List[List[int]] -> int

# Time Complexity: O(m * n) — every cell visited at most once.
# Space Complexity: O(m * n) — in worst case, all cells are in the queue.

from collections import deque

def traverse(q, matrix, directions, rows, cols, fresh):
    time = 0
    while q and fresh > 0:
        for i in range(len(q)):
            currI, currJ = q.popleft()

            for direction in directions:
                nextI = currI + direction[0]
                nextJ = currJ + direction[1]
                if 0 <= nextI < rows and 0 <= nextJ < cols and matrix[nextI][nextJ] == 1:
                    matrix[nextI][nextJ] = 2
                    q.append((nextI, nextJ))
                    fresh -= 1
        time += 1
    if fresh != 0:
        return -1
    else:
        return time
    
def orangesRotting(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
    q = deque()
    fresh = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i , j))
            elif grid[i][j] == 1:
                fresh += 1
    return traverse(q, grid, directions, rows, cols, fresh) 

#edge cases
# 1. Empty Grid
# Input: []
# Output: 0

# 2. No Oranges
# Input: [[0, 0], [0, 0]]
# Output: 0

# 3. All Oranges Already Rotten
# Input: [[2, 2], [2, 2]]
# Output: 0

# 4. All Oranges Fresh but No Rotten to Start
# Input: [[1, 1], [1, 1]]
# Output: -1

# 5. Some Fresh Can’t Be Reached
# Input: [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1

# 6. Normal Case - All Fresh Can Be Rotted
# Input: [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4


        