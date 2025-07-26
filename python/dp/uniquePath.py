# uniquePaths: int, int -> int
# Time Complexity: O(m * n), since we compute number of paths for each cell once.
# Space Complexity: O(m * n), due to the DP table storing results for each cell.

def uniquePaths(m, n):
    dp = []
    for i in range(m):
        dp.append([0] * (n))

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i - 1][j] 
            if j > 0:
                dp[i][j] += dp[i][j - 1] 

    return dp[m - 1][n - 1]

#edge cases
# 1. Smallest grid
# uniquePaths(1, 1) ➝ 1

# 2. One row
# uniquePaths(1, 5) ➝ 1

# 3. One column
# uniquePaths(5, 1) ➝ 1

# 4. Square grid
# uniquePaths(3, 3) ➝ 6

# 5. Rectangular grid
# uniquePaths(3, 7) ➝ 28

# 6. Large input
# uniquePaths(10, 10) ➝ 48620