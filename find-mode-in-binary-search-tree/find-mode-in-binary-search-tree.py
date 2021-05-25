# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return [] 
        
        d = {}
        q = deque([root])
        mostFreq = None
        count = 0 
        
        while q:
            size = len(q)
            
            for _ in range(size):
                curr = q.popleft()
                
                if curr.val not in d:
                    d[curr.val] = 0 
                
                d[curr.val] += 1 
                
                if d[curr.val] > count:
                    count = d[curr.val]
                    mostFreq = curr.val
                
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
                
        res = [] 
        for k, v in d.items():
            if v == count:
                res.append(k)
            
        
        return res
                 
                
        
        