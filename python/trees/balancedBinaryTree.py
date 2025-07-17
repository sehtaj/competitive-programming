# isBalanced: TreeNode -> bool

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1:
                return -1 

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        if height(root) == -1:
            return False
        else:
            return True
        
# edge cases

# 1. Empty Tree
# Input: None
# Output: True

# 2. Single Node
# Input: TreeNode(1)
# Output: True

# 3. Two Nodes (Unbalanced)
# Input:      1
#            /
#           2
# Output: True

# 4. Three Nodes (Linear)
# Input:      1
#            /
#           2
#          /
#         3
# Output: False

# 5. Perfectly Balanced Tree
# Input:       1
#             / \
#            2   3
# Output: True

# 6. Full Balanced Tree (3 Levels)
# Input:        1
#             /   \
#            2     3
#           / \   / \
#          4   5 6   7
# Output: True

        