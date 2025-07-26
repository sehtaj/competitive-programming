# maxProduct(nums: List[int]) -> int
# Time Complexity: O(n), where n is the number of elements in the input list.
# Space Complexity: O(1), constant space used for tracking current min, max, and result.

def maxProduct(nums):
    res = nums[0]
    curMin, curMax = 1, 1

    for num in nums:
        tmp = curMax * num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, num * curMin, num)
        res = max(res, curMax)
    return res

# Edge Case Tests:
# maxProduct([2, 3, -2, 4]) ➝ 6      (Product of [2, 3])
# maxProduct([-2, 0, -1]) ➝ 0        (Single 0 resets product)
# maxProduct([-2, 3, -4]) ➝ 24       (Negatives flip min/max)
# maxProduct([0, 2]) ➝ 2             (Zero followed by positive)
# maxProduct([-2]) ➝ -2              (Single negative number)