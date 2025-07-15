# findMaxAverage: List[int], int -> float

# Time Complexity: O(n)
# Space Complexity: O(1)

def findMaxAverage(nums,k):
    l = 0
    r = 0
    maxAvg = float('-inf')
    preSum = 0

    while r < len(nums):
        preSum = preSum + nums[r]
        if (r - l + 1) == k:
            maxAvg = max(maxAvg, preSum)
            preSum -= nums[l]
            l += 1
        r += 1

    return maxAvg / k


# edge cases
# findMaxAverage([1], 1)                           Expected: 1.0
# findMaxAverage([1,2,3,4,5], 5)                   Expected: 3.0
# findMaxAverage([1,12,-5,-6,50,3], 4)             Expected: 12.75
# findMaxAverage([-1,-2,-3,-4], 2)                 Expected: -3.0
# findMaxAverage([0,0,0,0,0,0], 3)                 Expected: 0.0
# findMaxAverage([7,4,5,6,8,2,1], 3)               Expected: 6.333333333333333
# findMaxAverage([10000,-10000,10000,-10000], 2)   Expected: 0.0
