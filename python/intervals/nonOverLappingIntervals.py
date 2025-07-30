# eraseOverlapIntervals(intervals: List[List[int]]) -> int

# Time Complexity: O(n log n), due to sorting
# Space Complexity: O(1), constant extra space

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0

    intervals.sort()

    count = 0  
    prevEnd = intervals[0][1]      

    for i in range(1, len(intervals)):  
        currStart = intervals[i][0] 
        currEnd = intervals[i][1]    

        if currStart >= prevEnd:     
            prevEnd = currEnd
        else:  
            count += 1  
            prevEnd = min(prevEnd, currEnd)   
    return count    

# edge cases
# 1. No overlapping intervals
# eraseOverlapIntervals([[1,2],[3,4],[5,6]]) -> 0

# 2. All intervals overlap with each other
# eraseOverlapIntervals([[1,5],[2,6],[3,7]]) -> 2

# 3. Some overlaps, need to remove few
# eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) -> 1

# 4. Single interval
# eraseOverlapIntervals([[1,10]]) -> 0

# 5. Intervals with same start
# eraseOverlapIntervals([[1,3],[1,2],[1,4]]) -> 2

# 6. Already sorted, overlapping
# eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5]]) -> 0