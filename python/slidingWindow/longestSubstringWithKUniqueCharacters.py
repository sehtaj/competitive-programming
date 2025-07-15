# longestKUniqueSubstring: str, int -> int

# Time Complexity: O(n)
# Space Complexity: O(k)

def longestKUniqueSubstring(s, k):
    l = 0
    r = 0
    hp = {}
    maxLen = 0

    while r < len(s):
        if s[r] in hp:
            hp[s[r]] += 1
        else:
            hp[s[r]] = 1

        while len(hp) > k:
            hp[s[l]] -= 1
            if hp[s[l]] == 0:
                del hp[s[l]]
            l += 1

        if len(hp) == k:
            maxLen = max(maxLen, r - l + 1)

        r += 1

    if maxLen == 0:
        return -1
    else:
        return maxLen
    
#edge cases
# longestKUniqueSubstring("aaabbbcccdddeeefff", 2)  Expected: 6
# longestKUniqueSubstring("aabacbebebe", 3)         Expected: 7
# longestKUniqueSubstring("aaaaa", 1)               Expected: 5
# longestKUniqueSubstring("abc", 4)                 Expected: -1
# longestKUniqueSubstring("", 2)                    Expected: -1
# longestKUniqueSubstring("abaccc", 1)              Expected: 3
# longestKUniqueSubstring("abaccc", 3)              Expected: 6
# longestKUniqueSubstring("abcdef", 3)              Expected: 3
