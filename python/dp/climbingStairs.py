# climbStairs: int -> int

# Time Complexity: O(n)
# Space Complexity: O(n)

def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# test cases
# climbStairs(1)    # Output: 1
# climbStairs(2)    # Output: 2
# climbStairs(3)    # Output: 3
# climbStairs(5)    # Output: 8
# climbStairs(10)   # Output: 89