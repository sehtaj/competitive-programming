# maxVowels: str, int -> int

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxVowels(s, k):
    l = 0 
    vowelCount = 0
    maxVowelCount = 0

    for r in range(len(s)):
        if s[r] == 'a' or s[r] == 'e' or s[r] == 'i' or s[r] == 'o' or s[r] == 'u':
            vowelCount += 1
        if (r - l + 1) == k:
            maxVowelCount = max(vowelCount, maxVowelCount)
            if s[l] == 'a' or s[l] == 'e' or s[l] == 'i' or s[l] == 'o' or s[l] == 'u':
                vowelCount -= 1
            l += 1

    return maxVowelCount

# edge cases
# maxVowels("a", 1)                          Expected: 1
# maxVowels("b", 1)                          Expected: 0
# maxVowels("aeiou", 5)                      Expected: 5
# maxVowels("aeiou", 2)                      Expected: 2
# maxVowels("abciiidef", 3)                  Expected: 3  ("iii")
# maxVowels("zzzzzzzzzz", 5)                 Expected: 0  (no vowels)
# maxVowels("aabecidofu", 5)                 Expected: 4  ("ecido")