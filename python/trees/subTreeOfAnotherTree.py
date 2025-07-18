# isSubtree: TreeNode, TreeNode -> bool
# Time Complexity: O(m * n) in the worst case (comparing every node in root with subRoot)
# Space Complexity: O(h), where h is the height of the main tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        if not root or not subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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
# root = None
# subRoot = None
# Output: False

# 2. Main Tree Empty, subRoot Non-Empty
# root = None
# subRoot = 1
# Output: False

# 3. subRoot is Empty
# root =     1
#           / \
#          2   3

# subRoot = None
# Output: True

# 4. root and subRoot are exactly the same
# root =     1
#           / \
#          2   3

# subRoot =  1
#           / \
#          2   3
# Output: True

# 5. subRoot is a leaf node
# root =       3
#             / \
#           4     5
#          / \
#         1   2

# subRoot = 1

# Output: True

# 6. Same values but different structure
# root =       3
#             / \
#           4     5
#          / \
#         1   2
# subRoot =   4
#            / \
#           2   1  # reversed
# Output: False

# 7. subRoot not found at all
# root =    1
#          / \
#         2   3
# subRoot = 4
# Output: False

