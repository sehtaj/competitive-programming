# minSubArrayLen: List[int], int -> int

# Time Complexity: O(n)
# Space Complexity: O(1)

def minSubArrayLen(nums, target):
    l = 0
    r = 0
    minSize = float('+inf')
    prevSum = 0

    while r < len(nums):
        prevSum = prevSum + nums[r]
        while prevSum >= target:
            minSize = min(minSize, r - l + 1 )
            prevSum = prevSum - nums[l]
            l += 1
        r += 1

    if minSize == float('+inf'):
        return 0
    else:
        return minSize
    
#edge cases
# minSubArrayLen(15, [1,2,3,4,5])        Expected: 5    
# minSubArrayLen(100, [1,1,1,1])         Expected: 0    
# minSubArrayLen(3, [1,1,1,1,1])         Expected: 3    
# minSubArrayLen(11, [1,2,3,4,5])        Expected: 3    
# minSubArrayLen(6, [10,2,3])            Expected: 1    
# minSubArrayLen(1, [1])                 Expected: 1    
# minSubArrayLen(2, [1])                 Expected: 0    
