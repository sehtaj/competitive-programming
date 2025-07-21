# numIslands: List[List[str]] -> int

# Time Complexity: O(m * n), where m = rows and n = cols
# Space Complexity: O(m * n), in the worst case all cells are '1' and visited

def numIslands(grid):
    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    directions = ((0,1), (0,-1), (-1,0), (1,0))
    count = 0

    for i in range(rows):
        for j in range(cols):
            if (i,j) not in visited and grid[i][j] == '1':
                traverse(grid, i, j, visited, directions)
                count += 1
    return count

def traverse(grid, i, j, visited, directions):
    stack = [(i,j)]
    rows = len(grid)
    cols = len(grid[0])

    while stack:
        currI, currJ = stack.pop()

        if (currI, currJ) in visited:
            continue

        visited.add((currI,currJ))

        for direction in directions:
            nextI = currI + direction[0]
            nextJ = currJ + direction[1]

            if 0 <= nextI < rows and  0 <= nextJ < cols and (nextI, nextJ) not in visited and grid[nextI][nextJ] == '1':
                stack.append((nextI, nextJ))

# 1. Empty Grid
# grid = []
# Output: 0

# 2. All Water
# grid = [
#   ["0", "0"],
#   ["0", "0"]
# ]
# Output: 0

# 3. One Big Island
# grid = [
#   ["1", "1"],
#   ["1", "1"]
# ]
# Output: 1

# 4. Diagonally Connected '1's (not an island)
# grid = [
#   ["1", "0"],
#   ["0", "1"]
# ]
# Output: 2

# 5. Multiple Small Islands
# grid = [
#   ["1", "0", "1", "0"],
#   ["0", "1", "0", "1"]
# ]
# Output: 4

# 6. Horizontal Island
# grid = [["1", "1", "1", "1", "0"]]
# Output: 1

# 7. Vertical Island
# grid = [
#   ["1"],
#   ["1"],
#   ["1"],
#   ["1"],
#   ["0"]
# ]
# Output: 1
            
