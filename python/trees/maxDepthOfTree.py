# maxDepth: TreeNode -> int

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        maximumDepth =  1 + max(rightDepth, leftDepth)

        return maximumDepth 
    
# edge cases

# 1. Empty Tree
# Input: None
# Output: 0

# 2. Single Node
# Input: TreeNode(1)
# Output: 1

# 3. Balanced Tree
# Input:    1
#         /   \
#        2     3
# Output: 2

# 4. Left-Heavy Tree
# Input:       1
#             /
#            2
#           /
#          3
# Output: 3