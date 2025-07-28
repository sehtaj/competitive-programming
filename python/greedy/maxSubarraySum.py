# maxSubArray(nums: List[int]) -> int

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubArray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)

    return maxSum

# edge cases
# 1. Single element
# maxSubArray([5]) -> 5

# 2. All negative numbers
# maxSubArray([-3, -2, -1]) -> -1

# 3. All positive numbers
# maxSubArray([1, 2, 3, 4]) -> 10

# 4. Mix of positive and negative numbers
# maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) -> 6

# 5. Large negative prefix
# maxSubArray([-10, -3, 5, 6]) -> 11

# 6. Max subarray is in the middle
# maxSubArray([1, -2, 3, 4, -1, 2, -5]) -> 8

