# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not self.dfs(root):
            return None 
        
        return root 
    
    def dfs(self, root):
        # base case 
        if not root:
            return False 
        
        # logic
        a1 = self.dfs(root.left)
        a2 = self.dfs(root.right)
        
        if not a1:
            root.left = None 
        
        if not a2:
            root.right = None 
        
        return root.val == 1 or a1 or a2