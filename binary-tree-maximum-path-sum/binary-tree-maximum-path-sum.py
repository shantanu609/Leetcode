# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res 
    
    def helper(self, root):
        # base case 
        if not root:
            return 0
        
        # logic 
        left_gain = max(self.helper(root.left), 0)
        right_gain = max(self.helper(root.right), 0)
        
        self.res = max(self.res, left_gain + right_gain + root.val)
        
        return root.val + max(left_gain, right_gain)
        
        