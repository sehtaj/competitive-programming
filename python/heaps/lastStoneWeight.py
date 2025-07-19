# lastStoneWeight: List[int] -> int

# Time Complexity: O(n log n), where n is the number of stones
# Space Complexity: O(n), for the heap

import heapq

class Solution:
    def lastStoneWeight(stones):
        maxHeap = []
        for i in range(0, len(stones)):
            stones[i] = -stones[i]
            maxHeap.append(stones[i])
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x - y != 0:
                heapq.heappush(maxHeap, x - y)

        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
        
# edge cases
# 1. Single Stone
# stones = [5]
# Output: 5

# 2. Two Equal Stones
# stones = [3, 3]
# Output: 0

# 3. Two Unequal Stones
# stones = [10, 4]
# Output: 6

# 4. All Stones Destroy Each Other
# stones = [2, 2, 2, 2]
# Output: 0

# 5. Large List with One Remaining
# stones = [9, 3, 2, 10]
# Output: 0

# 6. Empty List
# stones = []
# Output: 0

