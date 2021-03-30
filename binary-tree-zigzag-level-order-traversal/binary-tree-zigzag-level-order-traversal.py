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
        result = [] 
        
        q = deque()
        flag = False # for left to right 
        q.append(root)
        
        while q:
            size = len(q)
            temp = []
            if flag == False:
                # left to right 
                for _ in range(size):
                    curr = q.popleft()
                    temp.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                flag = True 
                result.append(temp)
            
            else:
                # right to left
                temp = [] 
                for _ in range(size):
                    curr = q.popleft()
                    temp.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
                temp = temp[::-1]
                result.append(temp)
                flag = False 
        
        return result
            

        