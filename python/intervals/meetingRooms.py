# canAttendMeetings(intervals: List[Interval]) -> bool

# Time Complexity: O(n log n), where n is the number of intervals (for sorting)
# Space Complexity: O(1), ignoring sort stack space

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        prev = intervals[i - 1]
        curr = intervals[i]
        if curr.start < prev.end:
            return False

    return True

# edge cases
# 1. No meetings — always possible to attend all
# canAttendMeetings([])   # True

# 2. Single meeting 
# canAttendMeetings([Interval(1, 2)])   # True

# 3. Two non-overlapping meetings
# canAttendMeetings([Interval(1, 2), Interval(3, 4)])   # True

# 4. Two overlapping meetings
# canAttendMeetings([Interval(1, 5), Interval(4, 6)])   # False

# 5. Meetings that touch at the boundary
# canAttendMeetings([Interval(1, 3), Interval(3, 5)])   # True

# 6. Meetings out of order but overlapping
# canAttendMeetings([Interval(5, 10), Interval(0, 6)])   # False