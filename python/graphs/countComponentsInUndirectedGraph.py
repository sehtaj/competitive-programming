# countComponents(n: int, edges: List[List[int]]) -> int

# Time Complexity: O(V + E), where V = number of nodes, E = number of edges
# Space Complexity: O(V + E), for adjacency list and visited array

def dfs(node, adj, visited):
    for neighbor in adj[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, adj, visited)

def countComponents(n, edges):
    adj = []
    for i in range(n):
        adj.append([])

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    count = 0

    for node in range(n):
        if not visited[node]:
            visited[node] = True
            dfs(node, adj, visited)
            count += 1

    return count

# edge cases
# 1. No edges (each node is its own component)
# countComponents(5, [])                            # Output: 5

# 2. Fully connected graph
# countComponents(5, [[0,1],[1,2],[2,3],[3,4]])     # Output: 1

# 3. Multiple components
# countComponents(5, [[0,1],[2,3]])                 # Output: 3

# 4. Single node
# countComponents(1, [])                            # Output: 1

# 5. Disconnected pairs
# countComponents(4, [[0,1],[2,3]])                 # Output: 2