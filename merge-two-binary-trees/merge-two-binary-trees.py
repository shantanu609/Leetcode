# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 :
            return root2 
        
        if not root2: 
            return root1 
        
        self.mergeHelper(root1, root2)
        return root1 
    
    def mergeHelper(self, root1, root2):
        # base case 
        if not root1 and not root2:
            return 
        
        if not root1:
            return root2 
        
        if not root2:
            return root1 
        
        # logic 
        root1.val = root1.val + root2.val
        
        root1.left = self.mergeHelper(root1.left, root2.left)
        root1.right = self.mergeHelper(root1.right, root2.right)
        
        return root1