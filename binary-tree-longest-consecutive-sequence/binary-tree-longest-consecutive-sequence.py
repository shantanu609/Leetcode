# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        self.res = 1
        
        self.dfsHelper(root)
        return self.res
    
    
    def dfsHelper(self, root):
        # base case 
        if not root:
            return 0
       
        # logic 
        l = 1 + self.dfsHelper(root.left)
        r = 1 + self.dfsHelper(root.right)
        
        if root and root.right and root.val + 1 != root.right.val:
            r = 1 
        
        if root and root.left and root.val + 1 != root.left.val:
            l = 1
        
        total = max(l , r)
        
        self.res = max(self.res, total)
        
        return total