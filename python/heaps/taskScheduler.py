# leastInterval: List[str], int -> int

# Time Complexity: O(n log n), where n = number of tasks (heap operations)
# Space Complexity: O(n), for heap and queue

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):
        hp = {}
        for i in tasks:
            if i in hp:
                hp[i] += 1
            else:
                hp[i] = 1

        maxHeap = []

        for i in hp.values():
            i = -i
            maxHeap.append(i)

        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
    

# edge cases
# 1. No cooldown required (n = 0)
# tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 0
# Output: 6

# 2. All tasks same, large cooldown
# tasks = ['A', 'A', 'A', 'A'], n = 3
# Output: 13 (A _ _ _ A _ _ _ A _ _ _ A)

# 3. Enough tasks to fill cooldown
# tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 2
# Output: 8 (A B _ A B _ A B)

# 4. Only one task
# tasks = ['A'], n = 2
# Output: 1

# 5. Multiple tasks with no repeats
# tasks = ['A', 'B', 'C', 'D'], n = 3
# Output: 4

# 6. Empty task list
# tasks = [], n = 2
# Output: 0
            



        
