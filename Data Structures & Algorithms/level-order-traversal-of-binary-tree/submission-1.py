from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        sol = []

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.pop()
                level.append(node.val)

                if node.left:
                    q.appendleft(node.left)
                
                if node.right:
                    q.appendleft(node.right)

            if len(level) != 0:
                sol.append(level)
                
        return sol
