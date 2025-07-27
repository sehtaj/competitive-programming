# coinChange(coins: List[int], amount: int) -> int

# Time Complexity: O(n * amount), where n is the number of coins
# Space Complexity: O(n * amount), due to the 2D DP table

def coinChange(coins, amount):
    dp = []

    n = len(coins)

    for i in range(n + 1):
        dp.append([0] * (amount + 1))

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(amount + 1):
            if coins[i-1] <= j:
                dp[i][j] = (dp[i][j - coins[i - 1]]) + (dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][amount]

# edge cases
# 1. No coins
# coinChange([], 3) -> 0

# 2. Amount is 0
# coinChange([1, 2, 3], 0) -> 1   

# 3. Coin value > amount
# coinChange([5], 3) -> 0

# 4. Only one way to form the amount
# coinChange([3], 3) -> 1

# 5. Multiple combinations
# coinChange([1, 2], 4) -> 3  
