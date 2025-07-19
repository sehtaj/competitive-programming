# findKthLargest: List[int], int -> int

# Time Complexity: O(n log k), where n is the number of elements in nums
# Space Complexity: O(k), for the heap

import heapq

class Solution:
    def findKthLargest(self, nums , k):
        
        heap = []
        for i in range(k):
            heap.append(nums[i])
        heapq.heapify(heap)  

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)        
                heapq.heappush(heap, nums[i]) 

        return heap[0]
    
# edge cases
# 1. Single element
# nums = [5], k = 1
# Output: 5

# 2. All elements are the same
# nums = [2, 2, 2, 2], k = 2
# Output: 2

# 3. K = length of array
# nums = [3, 1, 2, 4], k = 4
# Output: 1

# 4. K = 1 (find max)
# nums = [3, 2, 1, 5, 6, 4], k = 1
# Output: 6

# 5. Unsorted input
# nums = [7, 10, 4, 3, 20, 15], k = 3
# Output: 10

# 6. Negative numbers
# nums = [-1, -3, -2, -4, -5], k = 2
# Output: -2
    

