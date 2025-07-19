# KthLargest: maintains the k-th largest element in a stream
# Time Complexity:
#   - Constructor: O(n log n) for heapify
#   - add(): O(log k)
# Space Complexity: O(k), storing only k largest elements in the heap

import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#edge cases
# 1. Empty initial list
# Input:
# k = 1, nums = []
# obj = KthLargest(1, [])
# obj.add(5) -> Output: 5

# 2. Initial list shorter than k
# Input:
# k = 3, nums = [1]
# Heap after init: [1]
# obj.add(2) -> Output: 1
# obj.add(3) -> Output: 1
# obj.add(4) -> Output: 2

# 3. Initial list has exactly k elements
# Input:
# k = 2, nums = [4, 5]
# obj.add(3) -> Output: 4

# 4. Adding a value smaller than all in heap
# Input:
# k = 3, nums = [10, 20, 30]
# obj.add(5) -> Output: 10

# 5. Adding a value larger than the smallest
# Input:
# k = 3, nums = [10, 20, 30]
# obj.add(25) -> Output: 20

# 6. Adding a duplicate of existing element
# Input:
# k = 2, nums = [4, 4]
# obj.add(4) -> Output: 4

# 7. Adding the maximum possible number
# Input:
# k = 2, nums = [1, 2]
# obj.add(1_000_000_000) -> Output: 2