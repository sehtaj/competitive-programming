# findRedundantConnection: List[List[int]] -> List[int]

# Time Complexity: O(n^2), since for every edge we perform DFS in worst case
# Space Complexity: O(n), for the visited list and graph adjacency list

def dfs(node, parent, graph, visited):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, graph, visited):
                return True
        elif neighbor != parent:
            return True
    return False

def findRedundantConnection(edges):
    n = len(edges)
    graph = []
    for i in range(n + 1):
        graph.append([])

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        visited = [False] * (n + 1)
        if dfs(u, -1, graph, visited):
            return [u, v]
    return []

# edge cases
# 1. Minimum input size with a cycle
# findRedundantConnection([[1, 2], [2, 3], [1, 3]])  # Output: [1, 3]

# 2. Cycle is the last edge added
# findRedundantConnection([[1, 2], [1, 3], [2, 4], [3, 4]])  # Output: [3, 4]

# 3. Star shape with a cycle
# findRedundantConnection([[1, 2], [1, 3], [1, 4], [2, 3]])  # Output: [2, 3]

# 4. Cycle formed by last edge connecting back to earlier node
# findRedundantConnection([[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])  # Output: [1, 5]

# 5. Disjoint tree components joined with a cycle (edge forming loop at the end)
# findRedundantConnection([[1, 2], [3, 4], [2, 3], [4, 1]])  # Output: [4, 1]

# 6. Deep tree structure, cycle at lower level
# findRedundantConnection([[1, 2], [2, 3], [3, 4], [4, 5], [2, 5]])  # Output: [2, 5]