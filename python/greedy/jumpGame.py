# canJump(nums: List[int]) -> bool

# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(1), constant space for the goal pointer

def canJump(nums):
    goal = len(nums) - 1

    for i in range(goal - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    if goal == 0:
        return True
    else:
        return False

# edge cases
# 1. Single element, already at goal
# canJump([0]) -> True

# 2. Can jump directly to the end
# canJump([2, 0, 0]) -> True

# 3. Cannot reach end due to 0s
# canJump([3, 2, 1, 0, 4]) -> False

# 4. All 1s, slow but possible
# canJump([1, 1, 1, 1, 1]) -> True

# 5. Long jump over zero
# canJump([2, 0, 2, 0, 1]) -> True

# 6. Stuck at 0 from the start
# canJump([0, 2, 3]) -> False
