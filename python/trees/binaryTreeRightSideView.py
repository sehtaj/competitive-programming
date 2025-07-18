# rightSideView: TreeNode -> List[int]
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(w), where w is the maximum width of the tree (BFS queue)

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        q = deque([root])
        res = []

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
# edge cases
# 1. Empty Tree
# root = None
# Output: []

# 2. Single Node
# Tree:
#   1
# Output: [1]

# 3. All Right Nodes (right-skewed)
# Tree:
#   1
#    \
#     2
#      \
#       3
# Output: [1, 2, 3]

# 4. All Left Nodes (left-skewed)
# Tree:
#     1
#    /
#   2
#  /
# 3
# Output: [1, 2, 3]   # Rightmost at each level is still visible (only one per level)

# 5. Full Binary Tree
# Tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
# Output: [1, 3, 6]

# 6. Rightmost Node Missing at Lower Level
# Tree:
#        1
#       / \
#      2   3
#     /
#    4
# Output: [1, 3, 4]
