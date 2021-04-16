# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False 
        if not t:
            return True 
        
        # check if they both are symmetric 
        if self.isSymmetric(s, t):
            return True 
        
        # else find either the left or the right sub tree for symmetry 
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSymmetric(self, s, t):
        if not s and not t:
            return True 
        
        if not s or not t:
            return False 
        
        return s.val == t.val and self.isSymmetric(s.left, t.left) and self.isSymmetric(s.right, t.right)