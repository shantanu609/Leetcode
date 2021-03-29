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
        return self.helper(root.left, root.right)
    
    def helper(self, node1, node2):
        # base case 
        if not node1 and not node2:
            return True 
        
        if not node1 or not node2:
            return False 
        
        # logic 
        return (node1.val == node2.val) and (self.helper(node1.left, node2.right)) and (self.helper(node1.right, node2.left))        
