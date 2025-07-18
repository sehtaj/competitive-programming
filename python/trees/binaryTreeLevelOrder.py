# levelOrder: TreeNode -> List[List[int]]
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(w), where w is the max width of the tree (queue)

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
    
#edge cases
# 1. Empty Tree
# root = None
# Output: []

# 2. Single Node
# Tree:
#   1
# Output: [[1]]

# 3. Two Levels
# Tree:
#     1
#    / \
#   2   3
# Output: [[1], [2, 3]]

# 4. Three Levels, Complete Binary Tree
# Tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
# Output: [[1], [2, 3], [4, 5, 6]]

# 5. Left Skewed Tree
# Tree:
#     1
#    /
#   2
#  /
# 3
# Output: [[1], [2], [3]]

# 6. Right Skewed Tree
# Tree:
#   1
#    \
#     2
#      \
#       3
# Output: [[1], [2], [3]]