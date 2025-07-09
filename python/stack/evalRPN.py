# evalRPN: List[str] -> int

# Time Complexity: O(n)
# Space Complexity: O(n)

def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            res = a + b
            stack.append(res)

        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            res = b - a
            stack.append(res)

        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            res = a * b
            stack.append(res)

        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            res = int(b / a)
            stack.append(res)

        else:
            stack.append(int(i))
    return stack[-1]

#edge cases

#evalRPN(["2", "1", "+", "3", "*"])
# 2 + 1 = 3 -> 3 * 3 = 9 -> Output: 9

# evalRPN(["4", "13", "5", "/", "+"])
# 13 / 5 = 2 (truncate) -> 4 + 2 = 6 -> Output: 6

# evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# From earlier steps -> Output: 22

# evalRPN(["3", "-4", "+"])
# 3 + (-4) = -1 -> Output: -1

# evalRPN(["4", "2", "/"])
# 4 / 2 = 2 -> Output: 2

# evalRPN(["-4", "2", "/"])
# -4 / 2 = -2 -> Output: -2 (truncates correctly)

# evalRPN(["7", "-3", "/"])
# 7 / -3 = -2.333 -> truncate -> -2 -> Output: -2