# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [] 
        node = root 
        q = deque([node])
        res = [] 
        
        while q: 
            size = len(q)
            sum_ = 0 
            for _ in range(size):
                curr = q.popleft() 
                sum_ += curr.val 
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right: 
                    q.append(curr.right)
            
            res.append(sum_/size)
        
        return res
                
        
        