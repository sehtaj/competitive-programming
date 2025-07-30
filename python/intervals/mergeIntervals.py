# merge(intervals: List[List[int]]) -> List[List[int]]

# Time Complexity: O(n log n), due to sorting
# Space Complexity: O(n), for the result array

def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    res = []
    res.append(intervals[0]) 
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = res[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            res.append(current)
    return res

# edge cases
# 1. Minimum input length
# merge([[0, 0]])   -> [[0, 0]]

# 2. All intervals are the same
# merge([[1, 3], [1, 3], [1, 3]])   -> [[1, 3]]

# 3. Completely overlapping intervals
# merge([[1, 10], [2, 5], [3, 7], [6, 9]])   -> [[1, 10]]

# 4. Partially overlapping intervals
# merge([[1, 4], [4, 5]])   -> [[1, 5]]

# 5. No overlapping intervals
# merge([[1, 2], [3, 4], [5, 6]])   -> [[1, 2], [3, 4], [5, 6]]

# 6. Intervals with large range values (within constraint)
# merge([[0, 5000], [5000, 10000], [10000, 10000]])   -> [[0, 10000]]