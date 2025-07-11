# findMin: List[int] -> int

# Time Complexity: O(log n)
# Space Complexity: O(1)

def findMin(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] < nums[r]:
            r = m
        else:
            l = m + 1
    return nums[l]

# edge cases
# findMin([1, 2, 3, 4, 5])  
# Expected: 1

# findMin([4, 5, 6, 7, 0, 1, 2])  
# Expected: 0

# findMin([2, 3, 4, 5, 1])  
# Expected: 1

# findMin([10])  
# Expected: 10

# findMin([3, 1])  
# Expected: 1

# findMin([5, 6, 1, 2, 3, 4])  
# Expected: 1
