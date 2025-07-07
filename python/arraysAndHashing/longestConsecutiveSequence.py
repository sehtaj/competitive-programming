# longestConsecutive: List[int] -> int

# Time: O(n), where n is the number of elements in nums.
# Space: O(n), for storing all unique numbers in a hash set.

def longestConsecutive(nums):
    hashSet = set(nums)
    longest = 0

    for num in hashSet:
        if num - 1 not in hashSet:
            count = 1

            for i in range(1, len(nums)):
                if num + i in hashSet:
                    count += 1
                else:
                    break  

            longest = max(longest, count)

    return longest

# edge cases
# longestConsecutive([])             # Empty list, no elements
# longestConsecutive([1])         # Single element is itself a sequence
# longestConsecutive([1, 2, 0, 1])   # Duplicates present, sequence: 0, 1, 2
# longestConsecutive([100, 4, 200, 1, 3, 2])  # Sequence: 1, 2, 3, 4
# longestConsecutive([10, 30, 20])    # No consecutive elements, longest sequence is just one number
# longestConsecutive([1, 3, 5, 7])    # All elements are isolated, no consecutive runs
# longestConsecutive([5, 4, 3, 2, 1])   # Reversed sequence, still valid