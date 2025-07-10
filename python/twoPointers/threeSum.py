# threeSum :  List[int] -> List[List[int]]

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def threeSum(nums):
    nums.sort()   
    res = []

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue 

        while l < r:
            if nums[l] + nums[r] == -nums[i]:
                res.append([nums[i], nums[l], nums[r]])

                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                    
                l += 1
                r -= 1

            elif nums[l] + nums[r] < -nums[i]:
                l += 1
            else:
                r -= 1

    return res

#edge cases

# threeSum([])  
# Expected: []

# threeSum([1, 2])
# Expected: []

# threeSum([1, 2, -2, -1])
# Expected: []

# threeSum([0, 0, 0, 0])
# Expected: [[0, 0, 0]]

# threeSum([-1, 0, 1, 2, -1, -4]) 
# Expected: [[-1, -1, 2], [-1, 0, 1]]

# threeSum([-1000000, 500000, 500000]) 
# Expected: [[-1000000, 500000, 500000]]