# isValidBST: TreeNode -> bool
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(h), where h is the height of the tree (recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root):
        def isBst(root, minVal, maxVal):
            if not root:
                return True  

            if minVal is not None and root.val <= minVal:
                return False
            if maxVal is not None and root.val >= maxVal:
                return False
                
            isValidLeft = isBst(root.left, minVal, root.val)
            if not isValidLeft:
                return False

            isValidRight = isBst(root.right, root.val, maxVal)
            if not isValidRight:
                return False
            
            return True

        return isBst(root, None, None)
    
# edge cases
# 1. Empty Tree
# root = None
# Output: True

# 2. Single Node
# Tree:
#   1
# Output: True

# 3. Valid BST
# Tree:
#       2
#      / \
#     1   3
# Output: True

# 4. Invalid BST (left child > root)
# Tree:
#       5
#      / \
#     6   7
# Output: False

# 5. Invalid BST (right child <= root)
# Tree:
#       5
#      / \
#     1   5
# Output: False

# 6. Deeper Invalid Case (violation not at direct child)
# Tree:
#         10
#        /  \
#       5    15
#           /  \
#         6     20
# Output: False
# Explanation: 6 is in the right subtree of 10 but less than 10