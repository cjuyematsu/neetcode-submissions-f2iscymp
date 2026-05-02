# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        allNodes = self.getAllNodes(root)

        return allNodes[k - 1]
        
    def getAllNodes(self, node):
        if not node:
            return []
        
        return self.getAllNodes(node.left) + [node.val] + self.getAllNodes(node.right)