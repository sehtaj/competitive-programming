# minDistance(word1: str, word2: str) -> int

# Time Complexity: O(m * n), where m = len(word1), n = len(word2)
# Space Complexity: O(m * n), for the DP matrix

def minDistance(word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [] 
        for i in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(m + 1):
            dp[i][0] = i  
        for j in range(n + 1):
            dp[0][j] = j  

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = 1 + dp[i][j - 1]
                    delete = 1 + dp[i - 1][j]
                    replace = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(insert, delete, replace)

        return dp[m][n]

# edge cases
# 1. Both strings are empty
# minDistance("", "") -> 0

# 2. One string is empty
# minDistance("abc", "") -> 3

# 3. Both strings are the same
# minDistance("abc", "abc") -> 0

# 4. Completely different strings
# minDistance("abc", "xyz") -> 3

# 5. Strings with partial overlap
# minDistance("intention", "execution") -> 5

# 6. Single-character difference
# minDistance("horse", "ros") -> 3