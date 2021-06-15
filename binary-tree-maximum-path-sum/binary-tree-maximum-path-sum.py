# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        self.res = float('-inf')
        self.helper(root)
        return self.res 
    
    def helper(self, root):
        # base case 
        if not root:
            return 0 
        
        # Logic 
        l = max(0, self.helper(root.left))
        r = max(0, self.helper(root.right))
        
        total = root.val + l + r 
        
        self.res = max(self.res, total)
        
        return root.val + max(l , r)