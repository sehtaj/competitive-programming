# isValid: str → bool

# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):

    hp = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }

    stack = []

    for i in s:
        if i in hp:
            if stack and stack[-1] == hp[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if not stack:
        return True
    else:
        return False
    

# print(isValid("()"))         True
# print(isValid("()[]{}"))     True
# print(isValid("(]"))         False
# print(isValid("([)]"))       False
# print(isValid("{[]}"))       True
# print(isValid(""))           True 
    


