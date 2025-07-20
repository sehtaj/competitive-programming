# kthSmallest: TreeNode, int -> int

# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root, k):
        arr = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k - 1]
    
# 1. Single Node
# Tree:
#   5
# k = 1
# Output: 5

# 2. Left-Skewed Tree
# Tree:
#     3
#    /
#   2
#  /
# 1
# k = 2
# Output: 2

# 3. Right-Skewed Tree
# Tree:
# 1
#  \
#   2
#    \
#     3
# k = 3
# Output: 3

# 4. Complete BST
# Tree:
#      3
#     / \
#    1   4
#     \
#      2
# k = 3
# Output: 3

# 5. k == 1 (smallest)
# Tree:
#      5
#     / \
#    3   6
#   /
#  2
# k = 1
# Output: 2

# 6. k == n (largest)
# Tree:
#      3
#     / \
#    1   4
# k = 3
# Output: 4

