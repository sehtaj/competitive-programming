# productExceptSelf: List[int] -> List[int]

# Time: O(n), where n is the number of elements in the input list `nums`
# Space: O(n) for the output list; uses O(1) extra space


def productExceptSelf(nums):
    product = 1
    zero_count = 0

    for num in nums:
        if num != 0:
            product *= num
        else:
            zero_count += 1

    output = []
    for i in range(0,len(nums)):
        if zero_count > 1:
            output.append(0)  
        elif zero_count == 1:
            if nums[i] == 0:
                output.append(product) 
            else:
                output.append(0) 
        else:
            output.append(product // nums[i])  

    return output

