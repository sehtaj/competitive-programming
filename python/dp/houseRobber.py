# houseRobber(nums: List[int]) -> int

# Time Complexity: O(n), where n is the number of houses.
# Space Complexity: O(n), for the DP array.

def houseRobber(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    
    return dp[n - 1]

# edge cases
# 1. No houses
# houseRobber([])               # Output: 0

# 2. One house
# houseRobber([5])              # Output: 5

# 3. Two houses
# houseRobber([2, 3])           # Output: 3

# 4. Multiple houses
# houseRobber([2, 7, 9, 3, 1])  # Output: 12

# 5. All equal houses
# houseRobber([5, 5, 5, 5])     # Output: 10

# 6. Large gap between houses
# houseRobber([10, 1, 1, 10])   # Output: 20