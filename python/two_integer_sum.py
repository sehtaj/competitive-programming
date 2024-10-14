def two_integer_sum(nums,target):
    count = {}
    for i in range(0,len(nums)):
        num = nums[i]
        number = target - nums[i]
        if number in count:
            j = count[number]
            return [j,i]
        count[num] = i    
        

two_integer_sum([3,4,5,6],7)
two_integer_sum([4,5,6],10)
two_integer_sum([5,5],10)

