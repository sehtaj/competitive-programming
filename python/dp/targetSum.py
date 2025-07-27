# findTargetSumWays(nums: List[int], target: int) -> int

# Time Complexity: O(n * sum), where n is the number of elements and sum is (target + total) // 2
# Space Complexity: O(n * sum), for the DP table

def findTargetSumWays(nums, target):
    total = sum(nums)
    if abs(target) > total or (target + total) % 2 != 0:
        return 0
    sum1 = (target + total) // 2
    return countSubsetSum(nums, sum1)

def countSubsetSum( nums, target):
    n = len(nums)
    dp = []

    for i in range(n + 1):
        dp.append([0] * (target + 1))

    for i in range(n + 1):
        dp[i][0] = 1  

    for i in range(1, n + 1):
        for j in range(target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

# edge cases
# 1. Single element equals target
# findTargetSumWays([1], 1)                 # 1

# 2. Single element not equal to target
# findTargetSumWays([1], 2)                 # 0

# 3. Multiple ways to achieve target
# findTargetSumWays([1, 1, 1, 1, 1], 3)     # 5

# 4. Zero sum with zero elements
# findTargetSumWays([], 0)                  # 1

# 5. Target not reachable due to odd sum
# findTargetSumWays([1, 2, 3], 2)           # 1

# 6. Target exceeds total sum
# findTargetSumWays([1, 2, 7], 20)          # 0