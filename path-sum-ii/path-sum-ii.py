# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return [] 
        self.res = [] 
        self.dfs(root, targetSum, [], 0)
        return self.res
    
    def dfs(self, root, targetSum, path, rSum):
        # base case 
        if not root:
            return 
        
        # logic 
        # 1) action
        rSum += root.val 
        path.append(root.val)
        
        self.dfs(root.left, targetSum, path, rSum)
            # self.res.append(path.copy())
        
        self.dfs(root.right, targetSum, path, rSum)
            # self.res.append(path.copy())
        
        if rSum == targetSum and not root.left and not root.right: 
            self.res.append(path.copy())
        
        rSum -= root.val 
        path.pop()
        