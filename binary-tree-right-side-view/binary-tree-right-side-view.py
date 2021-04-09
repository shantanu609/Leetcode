# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return [] 
        node = root
        q = deque()
        q.append(node)
        res = []
        
        while q:
            size = len(q)
            curr = None 
            for _ in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            if curr:
                res.append(curr.val)
        
        return res
                