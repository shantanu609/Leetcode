# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return  0 
        
        q = deque([root])
        depth = 0
        
        while q: 
            size = len(q)
            depth += 1 
            
            for _ in range(size):
                curr = q.popleft() 
                
                if curr.right:
                    q.append(curr.right)
                
                if curr.left:
                    q.append(curr.left)
        
        return depth