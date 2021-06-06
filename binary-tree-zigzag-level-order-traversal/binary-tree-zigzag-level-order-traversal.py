# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = [] 
        q = deque([root])
        reverse = False 
        
        while q:
            temp = deque()
            size = len(q)
            
            for _ in range(size):
                curr = q.popleft() 
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                
                if curr.right: 
                    q.append(curr.right)
            
            if reverse: 
                output.append([])
                while temp:
                    output[-1].append(temp.pop())
                reverse = False 
            else: 
                output.append(list(temp).copy())
                reverse = True
        
        
        return output