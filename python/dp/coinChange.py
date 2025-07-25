# coinChange: List[int], int -> int

# Time Complexity: O(amount * n) where n is the length of coins
# Space Complexity: O(amount)
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1
    
# edge cases
# 1. Typical case
# coinChange([1, 2, 5], 11)  # Output: 3 

# 2. No possible combination
# coinChange([2], 3)        # Output: -1

# 3. Amount is 0
# coinChange([1], 0)        # Output: 0

# 4. Large coin that can't make amount
# coinChange([5, 10], 1)    # Output: -1

# 5. Only one coin that fits perfectly
# coinChange([7], 14)       # Output: 2
    
