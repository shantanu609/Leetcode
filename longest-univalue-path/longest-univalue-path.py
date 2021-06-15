# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0 
        self.helper(root)
        return self.res
    
    def helper(self, root):
        # base case 
        if not root:
            return 0 
        
        # Logic 
        left_length = self.helper(root.left)
        right_length = self.helper(root.right)
        
        l, r = 0, 0 
        
        if root.left and root.val == root.left.val: 
            l = left_length + 1 
        
        if root.right and root.val == root.right.val: 
            r = right_length + 1 
        
        self.res = max(self.res, l + r)
        
        return max(l, r)