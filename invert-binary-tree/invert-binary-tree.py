# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = [] 
        node = root 
        
        while node or stack:
            while node: 
                node.left, node.right = node.right, node.left 
                stack.append(node)
                node = node.left 
            
            curr = stack.pop()
#             if curr.right:
#                 stack.append(curr)
            
            node = curr.right
        
        return root
    
# Time = O(n)
# Space = O(n)
            
        
        
       