# search: List[int], int -> int

# Time Complexity: O(log n)
# Space Complexity: O(1)

def search(nums,target):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    pivot = l

    if nums[pivot] <= target and target <= nums[-1]:
        l = pivot
        r = len(nums) - 1
    else:
        l = 0
        r = pivot - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# edge cases
# search([4, 5, 6, 1, 2, 3], 1)     -> 3
# search([4, 5, 6, 7, 0, 1, 2], 3)  -> -1
# search([1, 2, 3, 4, 5], 4)        -> 3
# search([5], 5)                   -> 0
# search([5], 3)                   -> -1
# search([6, 1], 1)                -> 1
# search([6, 1], 6)                -> 0
# search([], 1)                    -> -1