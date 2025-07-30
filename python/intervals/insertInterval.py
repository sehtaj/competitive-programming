# insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]

# Time Complexity: O(n), where n is the number of intervals
# Space Complexity: O(n), for the output list

def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

#edge cases

# 1. Empty list of intervals
# insert([], [2, 5])  # ➝ [[2, 5]]

# 2. New interval goes at the end
# insert([[1, 2], [3, 5]], [6, 8])  # ➝ [[1, 2], [3, 5], [6, 8]]

# 3. New interval goes at the beginning
# insert([[5, 7], [8, 10]], [1, 3])  # ➝ [[1, 3], [5, 7], [8, 10]]

# 4. New interval overlaps all existing
# insert([[2, 3], [4, 5]], [1, 6])  # ➝ [[1, 6]]

# 5. New interval touches but doesn't overlap
# insert([[1, 2], [4, 5]], [2, 4])  # ➝ [[1, 5]]

# 6. New interval inside an existing interval
# insert([[1, 10]], [3, 4])  # ➝ [[1, 10]]