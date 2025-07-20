# goodNodes: TreeNode -> int

# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        
        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            if node.val >= maxSoFar:
                goodNode = 1
            else:
                goodNode = 0

            maxSoFar = max(maxSoFar, node.val)
            left = dfs(node.left, maxSoFar)
            right = dfs(node.right, maxSoFar)

            totalGoodNodes = left + right + goodNode
            return totalGoodNodes
        return dfs(root, root.val)
    
#edge cases
# 1. Single Node
# Tree:
#   5
# Output: 1 (the root is always a good node)

# 2. Increasing Path
# Tree:
#   1
#    \
#     2
#      \
#       3
# Output: 3 (all nodes are greater than previous)

# 3. Decreasing Path
# Tree:
#     3
#    /
#   2
#  /
# 1
# Output: 1 (only root is good)

# 4. All Nodes Equal
# Tree:
#     1
#    / \
#   1   1
# Output: 3 (every node is equal to max so far)

# 5. Mixed Tree
# Tree:
#       3
#      / \
#     1   4
#        / \
#       1   5
# Output: 4 (nodes 3, 4, 5, and 1 under left are good)

# 6. Empty Tree
# root = None
# Output: 0