# validTree: int, List[List[int]] -> bool

# Time Complexity: O(n), where n is the number of nodes (since it's a tree, edges = n - 1)
# Space Complexity: O(n), for storing the graph and visited set

def validTree(n, edges):
    if len(edges) != n - 1:
        return False

    graph = []

    for i in range(n):
        graph.append([])

    for edge in edges:
        a = edge[0]
        b = edge[1]
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    stack = [(0, -1)] 

    while stack:
        node, parent = stack.pop()

        if node in visited:
            return False  

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != parent:
                stack.append((neighbor, node))

    if len(visited) == n:
        return True
    else:
        return False
    
# 1. Single Node, No Edges (Valid Tree)
# validTree(1, [])  
# Expected: True

# 2. Two Nodes, One Edge (Valid Tree)
# validTree(2, [[0, 1]])  
# Expected: True

# 3. Two Nodes, No Edge (Disconnected)
# validTree(2, [])  
# Expected: False

# 4. Cycle Present (Invalid Tree)
# validTree(3, [[0, 1], [1, 2], [2, 0]])  
# Expected: False

# 5. Disconnected Graph (Not Fully Connected)
# validTree(4, [[0, 1], [2, 3]])  
# Expected: False

# 6. Valid Tree With 5 Nodes
# validTree(5, [[0,1],[0,2],[0,3],[1,4]])  
# Expected: True