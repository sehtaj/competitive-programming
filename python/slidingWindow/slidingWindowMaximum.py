# maxSlidingWindow: List[int], int -> List[int]

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSlidingWindow(nums, k):
    q = []  
    res = []

    for i in range(len(nums)):
        if q and q[0] < i - k + 1:
            q.pop(0)

        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res

# maxSlidingWindow([1], 1)                              Expected: [1]
# maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)       Expected: [3, 3, 5, 5, 6, 7]
# maxSlidingWindow([1, 2, 3, 4, 5], 1)                  Expected: [1, 2, 3, 4, 5]
# maxSlidingWindow([9, 8, 7, 6, 5], 2)                  Expected: [9, 8, 7, 6]
# maxSlidingWindow([4, 2, 12, 3], 3)                    Expected: [12, 12]
# maxSlidingWindow([7, 7, 7, 7, 7], 4)                  Expected: [7, 7]
# maxSlidingWindow([2, 1], 3)                           Expected: []     # k > len(nums)
# maxSlidingWindow([], 1)                               Expected: []     # empty input
# maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)               Expected: [3, 3, 2, 5]
# maxSlidingWindow([1, 3, 2, 5, 4], 5)                  Expected: [5]
# maxSlidingWindow([1, 2, 3, 4, 5], 4)                  Expected: [4, 5]
# maxSlidingWindow([3, 1, 3, 1, 3], 2)                  Expected: [3, 3, 3, 3]