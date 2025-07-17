# diameterOfBinaryTree: TreeNode -> int

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            pathLength = left + right
            if pathLength > self.diameter:
                self.diameter = pathLength

            return 1 + max(left, right)
        dfs(root)
        return self.diameter
    
# Edge Cases for diameterOfBinaryTree (for reference)

# 1. Empty Tree
# Input: None
# Output: 0

# 2. Single Node
# Input: TreeNode(1)
# Output: 0  (no edges)

# 3. Two Nodes
# Input:   1
#         /
#        2
# Output: 1

# 4. Linear Tree (Left-skewed)
# Input:      1
#           /
#         2
#       /
#     3
# Output: 2  (number of edges in the path 3 -> 2 -> 1)

# 5. Linear Tree (Right-skewed)
# Input: 1
#          \
#           2
#             \
#              3
# Output: 2

# 6. Balanced Tree
# Input:     1
#           / \
#          2   3
# Output: 2  (path: 2 -> 1 -> 3)

# 7. Full Tree (3 levels)
# Input:          1
#               /   \
#              2     3
#             / \   / \
#            4   5 6   7
# Output: 4  (longest path: 4 -> 2 -> 1 -> 3 -> 7)
    
