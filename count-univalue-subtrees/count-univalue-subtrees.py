# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        self.count = 0 
        self.helper(root, 0)
        return self.count 
    
    def helper(self, root, val):
        # base case 
        if not root:
            return True 
        
        # logic 
        left = self.helper(root.left, root.val)
        right = self.helper(root.right, root.val)
        
        if not left or not right:
            return False
        
        self.count += 1 
        
        return root.val == val