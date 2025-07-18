# lowestCommonAncestor: TreeNode, TreeNode, TreeNode -> TreeNode
# Time Complexity: O(h), where h is the height of the tree
# Space Complexity: O(h), due to recursion stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
        
# edge cases

# 1. Empty Tree
# Input:
# root = None
# p = TreeNode(1)
# q = TreeNode(2)
# Output: None

# 2. LCA is the Root
# Input:
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9
#       / \
#      3   5
# p = 2, q = 8
# Output: 6

# 3. One Node is Ancestor of the Other
# Input:
#         6
#        / \
#       2   8
#      / \
#     0   4
# p = 2, q = 4
# Output: 2

# 4. Both Nodes in Left Subtree
# Input:
#         6
#        / \
#       2   8
#      / \
#     0   4
#        / \
#       3   5
# p = 3, q = 5
# Output: 4

# 5. Both Nodes in Right Subtree
# Input:
#         6
#        / \
#       2   8
#          / \
#         7   9
# p = 7, q = 9
# Output: 8

# 6. Nodes Are the Same
# Input:
#         6
#        / \
#       2   8
# p = 2, q = 2
# Output: 2