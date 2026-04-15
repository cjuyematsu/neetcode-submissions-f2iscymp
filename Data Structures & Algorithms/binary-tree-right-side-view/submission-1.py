from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        sol = []

        while q:
            num_els = len(q)

            for i in range(num_els):
                el = q.popleft()

                if i == num_els - 1:
                    sol.append(el.val)
                
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            
        return sol
