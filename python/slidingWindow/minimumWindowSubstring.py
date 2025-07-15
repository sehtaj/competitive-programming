# minWindow: str, str -> str

# Time Complexity: O(n)
# Space Complexity: O(t)

def minWindow(s, t):
    if not s or not t:
        return ""

    hashmapT = {}
    for c in t:
        if c in hashmapT:
            hashmapT[c] += 1
        else:
            hashmapT[c] = 1

    hashmapS = {}
    l = 0
    r = 0
    formed = 0
    required = len(hashmapT)
    minLen = float('inf')
    minWindowStart = 0

    while r < len(s):
        if s[r] in hashmapS:
            hashmapS[s[r]] += 1
        else:
            hashmapS[s[r]] = 1

        if s[r] in hashmapT and hashmapS[s[r]] == hashmapT[s[r]]:
            formed += 1

        while formed == required:
            if r - l + 1 < minLen:
                minLen = r - l + 1
                minWindowStart = l

            hashmapS[s[l]] -= 1
            if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                formed -= 1
            l += 1

        r += 1

    if minLen != float('inf'):
        result = ""
        i = minWindowStart
        while i < minWindowStart + minLen:
            result += s[i]
            i += 1
        return result
    else:
        return ""

#edge cases
# minWindow("ADOBECODEBANC", "ABC")       Expected: "BANC"
# minWindow("a", "a")                     Expected: "a"
# minWindow("a", "aa")                    Expected: ""
# minWindow("aa", "aa")                   Expected: "aa"
# minWindow("ab", "b")                    Expected: "b"
# minWindow("abc", "ac")                  Expected: "abc"
# minWindow("abcde", "ed")                Expected: "de"
# minWindow("", "a")                      Expected: ""
# minWindow("a", "")                      Expected: ""
# minWindow("", "")                       Expected: ""
# minWindow("thisisatest", "tist")        Expected: "isatest"
# minWindow("abcabdebac", "cda")          Expected: "cabd"
# minWindow("aa", "aa")                   Expected: "aa"
# minWindow("aaabbbccc", "abc")           Expected: "abbbc"