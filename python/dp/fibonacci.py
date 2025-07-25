# fib(n: int) -> int

# Time Complexity: O(n)
# Space Complexity: O(n)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]

# edge cases
# fib(0)    # Output: 0
# fib(1)    # Output: 1
# fib(2)    # Output: 1
# fib(5)    # Output: 5
# fib(10)   # Output: 55
# fib(30)   # Output: 832040