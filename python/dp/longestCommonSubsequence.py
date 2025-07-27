# longestCommonSubsequence(x: str, y: str) -> int

# Time Complexity: O(n1 * n2), where n1 = len(x), n2 = len(y)
# Space Complexity: O(n1 * n2), for the DP table

def longestCommonSubsequence(x, y):
    n1 = len(x)
    n2 = len(y)

    dp = []
    for i in range(n1 + 1):
        row = []
        for j in range(n2 + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if (x[i - 1] == y[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n1][n2] 

# edge cases

# 1. One or both strings are empty
# longestCommonSubsequence("", "abc")        ->     0
# longestCommonSubsequence("abc", "")        ->     0
# longestCommonSubsequence("", "")           ->     0

# 2. No characters match
# longestCommonSubsequence("abc", "def")     ->     0

# 3. Exact same strings
# longestCommonSubsequence("abcde", "abcde") ->     5

# 4. Subsequence is non-contiguous
# longestCommonSubsequence("abcde", "ace")   ->     3

# 5. Repeated characters in one string
# longestCommonSubsequence("abcba", "abcbcba") ->   5

# 6. Interleaved common letters
# longestCommonSubsequence("aggtab", "gxtxayb") ->  4



