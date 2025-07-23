# findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]

# Time Complexity: O(V + E) where V = numCourses, E = len(prerequisites)
# Space Complexity: O(V + E) for the graph, visited/visiting sets, and recursion stack

def dfs( course, graph, visited, visiting, order):
    stack = []                  
    stack.append((course, False))  

    while stack:
        node, processed = stack.pop()

        if processed:
            visiting.discard(node)
            visited.add(node)
            order.append(node)
            continue

        if node in visiting:
            return True

        if node not in visited:
            stack.append((node, True))
            visiting.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, False))
                elif neighbor in visiting:
                    return True

    return False

def findOrder( numCourses: int, prerequisites):
    graph = {}
    for i in range(numCourses):
        graph[i] = []    

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()      
    visiting = set()    
    order = []           

    for course in range(numCourses):
        if course not in visited:
            if dfs(course, graph, visited, visiting, order):
                return []

    n = len(order)
    for i in range(n // 2):
        temp = order[i]
        order[i] = order[n - 1 - i]
        order[n - 1 - i] = temp
    return order

# edge cases
# 1. No prerequisites
# findOrder(2, [])                          # Output: [1,0] or [0,1]

# 2. Simple chain (0 <- 1 <- 2)
# findOrder(3, [[1,0], [2,1]])              # Output: [0,1,2]

# 3. Cycle present
# findOrder(2, [[0,1],[1,0]])               # Output: []

# 4. Independent components
# findOrder(4, [[1,0],[2,3]])               # Output: [0,1,3,2] or other valid topological sort

# 5. All courses depend on one
# findOrder(4, [[1,0],[2,0],[3,0]])         # Output: [0,1,2,3]

# 6. Fully connected DAG
# findOrder(4, [[1,0],[2,0],[3,1],[3,2]])   # Output: [0,1,2,3] or [0,2,1,3]