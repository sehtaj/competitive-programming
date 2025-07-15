def maxSlidingWindow(nums,k):
    l = 0
    r = k - 1
    res = []

    while r < len(nums):

        if len(nums) == 1:
            res.append(nums[l])
            return res

        elif nums[l] > nums[r] and nums[l] > nums[l + 1]:
            res.append(nums[l])

                                            #TBD


        elif nums[r] > nums[l] and nums[r] > nums[l + 1]:
            res.append(nums[r])

        else:
            res.append(nums[r - 1])

        l += 1
        r += 1 

    return res
