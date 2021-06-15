# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0 
        
        self.res = 0 
        self.helper(root, targetSum)
        return self.res 
    
    def helper(self, root, targetSum):
        # base case 
        if not root:
            return 
        
        # logic 
        self.dfs(root, targetSum, 0)
        
        self.helper(root.left, targetSum)
        
        self.helper(root.right, targetSum)
    
    
    def dfs(self, root, targetSum, rSum):
        # base case 
        if not root:
            return 
        
        # logic 
        rSum += root.val 
        
        self.dfs(root.left, targetSum, rSum)
        
        self.dfs(root.right, targetSum, rSum)
        
        if rSum == targetSum:
            self.res += 1 
        
        rSum -= root.val 