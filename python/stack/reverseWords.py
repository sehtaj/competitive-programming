#  reverseWords: str -> str

#  Time Complexity: O(n)
#  Space Complexity: O(n)

def reverseWords(s):

    words = s.split()
    stack = []
    for word in words:
        stack.append(word)

    result = ""

    while stack:
        if len(stack) == 1:
            result = result + (stack.pop())
        else:
            result = result + (stack.pop()) + ' '

    return result

#  edge cases
#  reverseWords("     ")           ->         ""
#  reverseWords("a")               ->         "a"
#  reverseWords("  a  ")            ->        "a"
#  reverseWords("word1  word2  word3") ->     "word3 word2 word1"
#  reverseWords(" hello   world again ") ->   "again world hello"
#  reverseWords("abc   ")           ->        "abc"
#  reverseWords("   abc")           ->        "abc"
#  reverseWords("")                 ->        ""
#  reverseWords("a b c d e")        ->        "e d c b a"