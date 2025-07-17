# isSameTree: TreeNode, TreeNode -> bool

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)

        if p.val != q.val:
            return False

        if leftTree is True and rightTree is True:
            return True
        else:
            return False
        

# edge cases

# 1. Both Trees Empty
# Input: p = None, q = None
# Output: True

# 2. One Tree Empty
# Input: p = TreeNode(1), q = None
# Output: False

# 3. Single Node, Same Value
# Input: p = TreeNode(1), q = TreeNode(1)
# Output: True

# 4. Single Node, Different Value
# Input: p = TreeNode(1), q = TreeNode(2)
# Output: False

# 5. Identical Structure & Values
# Input:    p       q
#           1       1
#          / \     / \
#         2   3   2   3
# Output: True

# 6. Same Structure, Different Values
# Input:    p       q
#           1       1
#          / \     / \
#         2   3   4   5
# Output: False

# 7. Different Structure
# Input:    p       q
#           1       1
#          /         \
#         2           2
# Output: False
