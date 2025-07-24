# minCostClimbingStairs(cost: List[int]) -> int

# Time Complexity: O(n)
# Space Complexity: O(n)

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    
    return dp[n]

# edge cases
# 1. Minimum input size
# minCostClimbingStairs([10, 15])              # Output: 10

# 2. Simple increasing cost
# minCostClimbingStairs([10, 15, 20])          # Output: 15

# 3. Equal cost steps
# minCostClimbingStairs([5, 5, 5, 5])          # Output: 10

# 4. Zero cost edge case
# minCostClimbingStairs([0, 0, 0, 1])          # Output: 0

# 5. Large cost at start
# minCostClimbingStairs([100, 1, 1, 1])        # Output: 2