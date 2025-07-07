def twoSum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        
        elif nums[l] + nums[r] < target:
            l += 1
        else: 
            r -= 1
    
print(twoSum([1,2,3,4], 7))
print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))

    