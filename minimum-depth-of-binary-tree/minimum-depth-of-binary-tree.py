# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        node = root
        q = deque([node])
        
        res = 0
        
        while q: 
            size = len(q)
            res += 1 
            for _ in range(size):
                curr = q.popleft() 
                if not curr.left and not curr.right: 
                    return res 
            
                if curr.left: 
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right) 
        
        return res
                 
        