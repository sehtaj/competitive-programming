def dailyTemperature(temperatures):
    answer = [0] * (len(temperatures))
    stack = []

    for i in range(0, len(temperatures)):

        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx 

        stack.append(i)
    return answer
            

print(dailyTemperature([73,74,75,71,69,72,76,73]))