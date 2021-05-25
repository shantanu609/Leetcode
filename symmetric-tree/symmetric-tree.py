# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True 
        
        q = deque([root])
        
        while q:
            size = len(q)
            p1, p2 = 0, size - 1 
            while p1 <= p2 :
                if not q[p1] and not q[p2]:
                    p1 += 1 
                    p2 -= 1
                    continue 
                    
                if (not q[p1] and q[p2]) or (q[p1] and not q[p2]) or (q[p1].val != q[p2].val):
                    return False 
            
                p1 += 1 
                p2 -= 1 
            
            for _ in range(size):
                curr = q.popleft()
                
                if curr and curr.left:
                    q.append(curr.left)
                elif curr and not curr.left:
                    q.append(None)
                
                if curr and curr.right:
                    q.append(curr.right)
                elif curr and not curr.right: 
                    q.append(None)
        
        return True 
                
                
                
                