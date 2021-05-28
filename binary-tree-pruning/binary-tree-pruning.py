# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None 
        
        if self.dfs(root):
            return root 
        return None 
    
    def dfs(self, node):
        # base case 
        if not node:
            return False 
        
        # logic 
        a1 = self.dfs(node.left)
        a2 = self.dfs(node.right)

        if not a1:
            node.left = None 
        
        if not a2:
            node.right = None 
        
        return node.val == 1 or a1 or a2