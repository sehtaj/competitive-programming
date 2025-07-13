# lengthOfLongestSubstring: str -> int

# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(m), where m is the number of unique characters in the string

def lengthOfLongestSubstring(s):
    l = 0
    r = 0
    hp = {}
    maxLen = 0

    while r < len(s):
        if s[r] not in hp or hp[s[r]] < l:
            hp[s[r]] = r
            length = r - l + 1
            maxLen = max(length, maxLen)
            r += 1

        else:
            l = hp[s[r]] + 1

    return maxLen

# edge cases
# lengthOfLongestSubstring("a")                  Expected: 1
# lengthOfLongestSubstring("aaaaa")              Expected: 1
# lengthOfLongestSubstring("abcdefg")            Expected: 7
# lengthOfLongestSubstring("abcdeafgh")          Expected: 7 ("bcdeafg")
# lengthOfLongestSubstring("abcabcbb")           Expected: 3 ("abc")
# lengthOfLongestSubstring("aabcbdeafgh")        Expected: 8 ("cbdeafgh")
# lengthOfLongestSubstring("abba")               Expected: 2 ("ab" or "ba")