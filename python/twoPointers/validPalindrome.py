# isPalindrome: str -> bool

# Time Complexity: O(n)
# Space Complexity: O(n)

def isPalindrome(str):
    res = ""

    for i in range(0,len(str)):
        if str[i].isalnum():
            res += str[i]
        
    res = res.lower()

    l = 0
    r = len(res) - 1

    while l < r:
        if res[l] != res[r]:
            return False
        else:
            l += 1
            r -= 1
    return True 

# edge cases

# isPalindrome("")                        True   # empty string is a palindrome
# isPalindrome("a")                       True   # single character
# isPalindrome("A man, a plan, a canal: Panama" True
# isPalindrome("race a car")             False
# isPalindrome("!!@#")                   True   # only symbols, filtered to empty string
# isPalindrome("0P")                     False  # '0' ≠ 'p'