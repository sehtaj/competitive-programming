# characterReplacement: str, int -> int

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1)

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    r = 0
    res = 0
    hp = {}
    maxFreq = 0

    while r < len(s):
        if s[r] in hp:
            hp[s[r]] += 1
        else:
            hp[s[r]] = 1

        if hp[s[r]] > maxFreq:
            maxFreq = hp[s[r]]

        while (r - l + 1) - maxFreq > k:
            hp[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res

# edge cases
# characterReplacement("ABAB", 2)       Expected: 4
# characterReplacement("AABABBA", 1)    Expected: 4 
# characterReplacement("ABCDE", 1)      Expected: 2
# characterReplacement("ABBB", 2)       Expected: 4
# characterReplacement("BAAAB", 2)      Expected: 5

