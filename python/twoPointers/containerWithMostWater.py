def maxArea(height):
    l = 0
    r = len(height) - 1
    maximumArea = 0

    while l < r:
        length = r - l
        breadth = min(height[l], height[r])
        area = length * breadth
        maximumArea = max(area, maximumArea)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maximumArea

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([3,6,1]))

