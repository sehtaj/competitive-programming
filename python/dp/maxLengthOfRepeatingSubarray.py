# findlength(x: str, y: str) -> int

# Time Complexity: O(n * m), where n and m are lengths of x and y.
# Space Complexity: O(n * m), for the DP table.

def findlength(x, y):
    n = len(x)
    m = len(y)

    dp = []

    for i in range(n + 1):
        dp.append([0] * (m + 1))
        
    maxLen = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (x[i - 1] == y[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
                maxLen = max(maxLen, dp[i][j])

            else:
                dp[i][j] = 0

    return maxLen

# edge cases
# 1. Both strings are empty
# findlength("", "")              ->    0

# 2. One string is empty
# findlength("abc", "")           ->    0
# findlength("", "xyz")           ->    0

# 3. No common substring
# findlength("abc", "def")        ->    0

# 4. Exact match
# findlength("abcde", "abcde")    ->    5

# 5. Partial match (substring in middle)
# findlength("xyzabc", "abc")     ->    3

# 6. Multiple common substrings (but only longest is counted)
# findlength("abcdfgh", "abedfgh") ->   3  


