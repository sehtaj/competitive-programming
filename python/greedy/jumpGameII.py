# jump(nums: List[int]) -> int

# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(1), constant space used for pointers

def jump(nums):
    left, right = 0, 1
    jumps = 0
    while right < len(nums):
        newRight = right
        for i in range(left, right):
            newRight = max(newRight, i + nums[i])
            
        left = right
        right = newRight + 1
        jumps += 1
    
    return jumps

# edge cases
# 1. Already at the end
# jump([0]) -> 0

# 2. One jump needed
# jump([2, 1]) -> 1

# 3. Must jump over zero
# jump([2, 0, 1]) -> 1

# 4. Multiple jumps, normal case
# jump([2, 3, 1, 1, 4]) -> 2

# 5. Max jump each time
# jump([5, 4, 3, 2, 1, 0]) -> 1

# 6. Gradual jumps
# jump([1, 1, 1, 1, 1]) -> 4