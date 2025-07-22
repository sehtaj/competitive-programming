# pacificAtlantic: List[List[int]] -> List[List[int]]

# Time Complexity: O(m * n), where m is number of rows and n is number of columns
# Space Complexity: O(m * n), for visited sets and recursion/queue space

from collections import deque

def bfs(q ,rows, cols, heights, directions):
    reachable = set()

    while q:
        currRow, currCol = q.popleft()
        if (currRow, currCol) in reachable:
            continue
        reachable.add((currRow, currCol))

        for direction in directions:
            nextRow, nextCol = currRow + direction[0], currCol + direction[1]
            if (0 <= nextRow < rows and 0 <= nextCol < cols and (nextRow, nextCol) not in reachable
                and heights[nextRow][nextCol] >= heights[currRow][currCol]):
                q.append((nextRow, nextCol))
    return reachable

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    rows = len(heights)
    cols = len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pacificQueue = deque()
    atlanticQueue = deque()

    for r in range(rows):
        pacificQueue.append((r, 0))
        atlanticQueue.append((r, cols - 1))
        
    for c in range(cols):
        pacificQueue.append((0, c))
        atlanticQueue.append((rows - 1, c))

    pacificReachable = bfs(pacificQueue, rows, cols, heights, directions)
    atlanticReachable = bfs(atlanticQueue, rows, cols, heights, directions)
    
    result = []
    for cell in pacificReachable:
        if cell in atlanticReachable:
            row = cell[0]
            col = cell[1]
            result.append([row, col])
    return result

#edge cases
# 1. Empty Grid
# pacificAtlantic([])  
# Expected: []

# 2. One Cell Grid
# pacificAtlantic([[0]])  
# Expected: [[0, 0]]

# 3. All Cells Same Height
# pacificAtlantic([[1,1],[1,1]])  
# Expected: [[0,0],[0,1],[1,0],[1,1]]

# 4. Surrounded Center (higher edges, low center)
# pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]])  
# Expected: [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]

# 5. Strictly Increasing from Top-Left to Bottom-Right
# pacificAtlantic([[1,2,3],[4,5,6],[7,8,9]])  
# Expected: [[0,2],[1,2],[2,2],[2,1],[2,0]]

# 6. Single Column Grid
# pacificAtlantic([[1],[2],[3]])  
# Expected: [[0,0],[1,0],[2,0]]
