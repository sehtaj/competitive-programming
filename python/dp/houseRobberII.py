# rob(nums: List[int]) -> int

# Time Complexity: O(n)
# Space Complexity: O(n)

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp1 = [0] * n
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

    dp2 = [0] * n
    dp2[0] = nums[1]
    dp2[1] = max(nums[1], nums[2])
    for i in range(2, n - 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])

    return max(dp1[n - 2], dp2[n - 2])

# edge cases
# 1. One house
# rob([10])                     # Output: 10

# 2. Two houses
# rob([5, 15])                  # Output: 15

# 3. Three houses (circular)
# rob([2, 3, 2])                # Output: 3

# 4. Four houses
# rob([1, 2, 3, 1])             # Output: 4

# 5. Larger input
# rob([2, 7, 9, 3, 1])          # Output: 11

# 6. Equal values
# rob([5, 5, 5, 5, 5])          # Output: 10