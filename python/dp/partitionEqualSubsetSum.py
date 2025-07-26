# canPartition: List[int] -> bool
 
# Time Complexity: O(n * target), where n = len(nums), target = total sum // 2
# Space Complexity: O(n * target), for the 2D dp array

def canPartition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)

    dp = []
    for i in range(n + 1):
        dp.append([False] * (target + 1))

    for i in range (n + 1):
        dp[i][0] = True

    for i in range(1 ,n + 1):
        for j in range(target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] or dp[i- 1][j- nums[i-1]])

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n, target]

# edge cases
# 1. Total sum is odd -> cannot partition
# canPartition([1, 2, 3]) -> False

# 2. Total sum is even, and partition is possible
# canPartition([1, 5, 11, 5]) -> True

# 3. Only one element
# canPartition([100]) -> False

# 4. All equal elements
# canPartition([2, 2, 2, 2]) -> True

# 5. Duplicate numbers, possible partition
# canPartition([1, 2, 5]) -> False

# 6. Empty input (technically invalid per constraints, but for robustness)
# canPartition([]) -> False

    