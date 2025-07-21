# maxAreaOfIsland: List[List[int]] -> int

# Time Complexity: O(m * n), where m is rows and n is cols
# Space Complexity: O(m * n)

def traverse(matrix, i, j, visited, directions):
    stack = [(i,j)]
    rows = len(matrix)
    cols = len(matrix[0])
    area = 0

    while stack:
        currI, currJ = stack.pop()

        if (currI, currJ) in visited:
            continue

        visited.add((currI,currJ))
        area += 1

        for direction in directions:
            nextI = currI + direction[0]
            nextJ = currJ + direction[1]

            if 0 <= nextI < rows and  0 <= nextJ < cols and (nextI, nextJ) not in visited and matrix[nextI][nextJ] == 1:
                stack.append((nextI, nextJ))

    return area

def maxAreaOfIsland(self, grid):
        if not grid:
            return []
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        directions = ((0,1), (0,-1), (-1,0), (1,0))
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 1:
                    area = traverse(grid, i, j, visited, directions)
                    maxArea = max(area, maxArea)
        return maxArea


# edge cases
# 1. Empty Grid
# grid = []
# Output: 0

# 2. All Water
# grid = [
#   [0, 0],
#   [0, 0]
# ]
# Output: 0

# 3. One Island
# grid = [
#   [1, 1],
#   [1, 0]
# ]
# Output: 3

# 4. Multiple Disconnected Islands
# grid = [
#   [1, 0, 0, 1],
#   [0, 1, 1, 0]
# ]
# Output: 2

# 5. Diagonal Connection (Not Valid)
# grid = [
#   [1, 0],
#   [0, 1]
# ]
# Output: 1 (diagonal is not considered connected)

# 6. Large Island Surrounded by Water
# grid = [
#   [0, 1, 0],
#   [1, 1, 1],
#   [0, 1, 0]
# ]
# Output: 5