# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.checkHelper(p, q)
    
    def checkHelper(self, p, q):
        # base case
        if not p and not q:
            return True 
        
        if (not p and q) or (p and not q) or (p.val != q.val):
            return False
        
        # logic 
        return self.checkHelper(p.left, q.left) and self.checkHelper(p.right, q.right)
        