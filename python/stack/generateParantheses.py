# generateParantheses: int -> List[str]

# Time Complexity: O(4^n / √n)
# Space complexity: O(n)


def generateParantheses(n):
    stack = [("", 0, 0)]  
    res = []

    while stack:
        curr, openN, closedN = stack.pop()

        if openN == closedN == n:
            res.append(curr)
            continue

        if openN < n:
            stack.append((curr + "(", openN + 1, closedN))

        if closedN < openN:
            stack.append((curr + ")", openN, closedN + 1))

    return res


#test cases
# generateParantheses(1)
# Output: ["()"]

# generateParantheses(2)
# Output: ["(()),"()()"]

# generateParantheses(3)
# Output: ["((()))","(()())","(())()","()(())","()()()"]

