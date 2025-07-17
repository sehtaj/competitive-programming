# invertTree: TreeNode -> TreeNode

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
# edge cases

# 1. Empty Tree
# Input: None
# Output: None

# 2. Single Node
# Input: TreeNode(1)
# Output: TreeNode(1)

# 3. Only Left Child
# Input:    1
#          /
#         2

# Output:   1
#             \
#              2

# 4. Only Right Child
# Input: 1
#          \
#           2

# Output:   1
#          /
#         2

# 5. Left-Heavy Tree
# Input:      1
#            /
#           2
#          /
#         3

# Output:     1
#              \
#               2
#                \
#                 3
