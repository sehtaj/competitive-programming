# canFinish: int, List[List[int]] -> bool

# Time Complexity: O(V + E), where V = numCourses and E = number of prerequisite pairs.
# Space Complexity: O(V + E), for the adjacency list and recursion stack.

def dfs(course, preMap, visiting):
    if course in visiting:
        return False
    if course not in preMap or preMap[course] == []:
        return True

    visiting.add(course)
    for pre in preMap[course]:
        if not dfs(pre, preMap, visiting):
            return False
    visiting.remove(course)
    preMap[course] = []
    return True

def canFinish(numCourses, prerequisites):
    preMap = {}
    for pair in prerequisites:
        course = pair[0]
        pre = pair[1]
        if course not in preMap:
            preMap[course] = []
        preMap[course].append(pre)

    visiting = set()

    for c in range(numCourses):
        if not dfs(c, preMap, visiting):
            return False
    return True

#edge cases
# 1. No Courses
# canFinish(0, [])  # True

# 2. No Prerequisites
# canFinish(3, [])  # True

# 3. Single Course With Its a Prerequisite (Cycle)
# canFinish(1, [[0, 0]])  # False

# 4. Simple Cycle
# canFinish(2, [[0, 1], [1, 0]])  # False

# 5. Valid Acyclic Dependencies
# canFinish(4, [[1, 0], [2, 1], [3, 2]])  # True

# 6. Disconnected Components With and Without Cycles
# canFinish(5, [[1, 0], [2, 3], [3, 2]])  # False