# kClosest: List[List[int]], int -> List[List[int]]

# Time Complexity: O(n log n), due to heapify and popping k elements
# Space Complexity: O(n), for storing all points in the heap

import heapq
import math

class Solution:
    def kClosest(self, points, k):
        minHeap = []
        
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((x ** 2) + (y ** 2))  
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)

        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
        
        return result
    
#edge cases
# 1. Empty input list
# points = [], k = 0
# Output: []

# 2. k = 0 (don't need any points)
# points = [[1, 2], [3, 4]], k = 0
# Output: []

# 3. k == len(points) (return all points)
# points = [[1, 2], [3, 4]], k = 2
# Output: [[1, 2], [3, 4]] or in heap order

# 4. All points at same distance
# points = [[1, 1], [-1, -1], [1, -1]], k = 2
# Output: Any 2 points (distances are equal)

# 5. Multiple close points, verify sorting by distance
# points = [[1, 1], [0, 0], [5, 5]], k = 2
# Output: [[0, 0], [1, 1]]

# 6. Negative coordinates
# points = [[-2, -4], [-1, -1], [3, 3]], k = 2
# Output: [[-1, -1], [3, 3]]