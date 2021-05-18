# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [] 
        node = root 
        
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node)
                node = node.left 
            
            elif stack:
                node = stack.pop()
                node = node.right 
            
        return res