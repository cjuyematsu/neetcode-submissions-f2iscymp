# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxx, node):
            if node is None:
                return 0
            
            if node.val >= maxx:
                return 1 + dfs(node.val, node.left) + dfs(node.val, node.right)
            
            else:
                return dfs(maxx, node.left) + dfs(maxx, node.right)

        return dfs(float('-inf'), root)
                