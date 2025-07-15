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