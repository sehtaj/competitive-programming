# dailyTemperature : List[int] -> List[int]

# Time Complexity: O(n) 
# Space Complexity: O(n)

def dailyTemperature(temperatures):
    answer = [0] * (len(temperatures))
    stack = []

    for i in range(0, len(temperatures)):

        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx 

        stack.append(i)
    return answer
            

# dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

# dailyTemperature([30, 40, 50, 60])
# Output: [1, 1, 1, 0]

# dailyTemperature([60, 50, 40, 30])
# Output: [0, 0, 0, 0]

# dailyTemperature([50, 50, 50, 50])
# Output: [0, 0, 0, 0]

# dailyTemperature([30, 31, 30, 29, 35])
# Output: [1, 3, 2, 1, 0]

# dailyTemperature([70])
# Output: [0]

# dailyTemperature([])
# Output: []