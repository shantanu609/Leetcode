# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 1 
        self.res = 0 
        
        def dfsHelper(root):
            # base case 
            if not root:
                return 0
            
            
            # logic 
            l = 1 + dfsHelper(root.left)
            r = 1 + dfsHelper(root.right) 
            
            if root.left and root.left.val != root.val + 1:
                l = 1 
            
            if root.right and root.right.val != root.val + 1:
                r = 1
                
            
            total = max(l, r)
            
            self.res = max(self.res, total)
            
            return total

        
        dfsHelper(root)
        return self.res