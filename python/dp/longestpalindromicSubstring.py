# longestPalindrome: str -> str

# Time Complexity: O(n^2), where n is the length of the string
# Space Complexity: O(1) for variables (i

def longestPalindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:  
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:  
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return res

#edge cases
# 1. Empty string
# longestPalindrome("") -> ""

# 2. All characters same
# longestPalindrome("aaaaa") -> "aaaaa"

# 3. No palindrome longer than 1
# longestPalindrome("abc") -> "a" (or "b" or "c")

# 4. Palindrome in the middle
# longestPalindrome("abcbade") -> "abcba"

# 5. Entire string is a palindrome
# longestPalindrome("racecar") -> "racecar"

# 6. Even-length palindrome
# longestPalindrome("cbbd") -> "bb"

# 7. Multiple palindromes, return the longest
# longestPalindrome("abaxyzzyxf") -> "xyzzyx"
