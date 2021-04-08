# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        self.res = float('-inf')
        self.dfs(root)
        return self.res 
    
    def dfs(self, node):
        # base case 
        if not node:
            return 0
        
        # logic 
        left, right = 0, 0 
        if node.left and node.left.val > 0:
            left = node.left.val 
        
        if node.right and node.right.val > 0:
            right = node.right.val 
        
        left = max(self.dfs(node.left) ,0)
        right = max(self.dfs(node.right), 0)
        
        total = max(node.val, node.val + left, node.val + right, node.val + left + right)
        # print("left = ", left, " right = ", right, " node.val = ",node.val)
        path = max(node.val + left, node.val + right)
        self.res = max(self.res, total)
        
        return path
        