# maxArea: List[int] -> int

# Time Complexity: O(n)
# Space Complexity: O(1)

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

#edge cases
# maxArea([])              => 0         # No lines
# maxArea([1])             => 0         # Only one line
# maxArea([1,1])           => 1         # Two equal lines
# maxArea([1,8,6,2,5,4,8,3,7])  =>49    # General case
# maxArea([5,4,3,2,1])      =>  6         # Decreasing heights

