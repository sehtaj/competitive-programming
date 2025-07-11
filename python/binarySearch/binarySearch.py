# binarySearch: List[int], int -> int

# Time Complexity: O(log n)
# Space Complexity: O(1)

def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  


# edge cases
# binarySearch([], 3)                    Empty list -> -1
# binarySearch([5], 5)                   One element, target present -> 0
# binarySearch([5], 3)                   One element, target absent -> -1
# binarySearch([2, 4, 6, 8], 2)           Target is the first element -> 0
# binarySearch([2, 4, 6, 8], 8)           Target is the last element -> 3
# binarySearch([1, 3, 5, 7, 9], 5)        Target is in the middle -> 2
# binarySearch([1, 3, 5, 7, 9], 6)        Target not in list -> -1
# binarySearch([1, 2, 2, 2, 3], 2)        Duplicates -> could be 1, 2, or 3
