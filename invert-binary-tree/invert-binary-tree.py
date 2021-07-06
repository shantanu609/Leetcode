# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root 
        
        self.helper(root)
        return root 
    
    
    def helper(self, root):
        # base case 
        if not root:
            return 
        
        # logic 
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        root.left = right 
        root.right = left 
        
        return root 