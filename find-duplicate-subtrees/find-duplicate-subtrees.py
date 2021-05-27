# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return [] 
        
        self.d = {} 
        self.res = [] 
        self.postOrderHelper(root, [])
        return self.res 
    
    
    def postOrderHelper(self, root, path):
        # base case 
        if not root:
            return ['#']
        
        # logic 
        path = self.postOrderHelper(root.left, path) + [' '] +self.postOrderHelper(root.right, path) + [' ']+ [str(root.val)]
        
        total = ''.join(path)
        
        if total in self.d and self.d[total] == 1:
            # time to add this duplicate to our result 
            self.res.append(root)
        
        if total not in self.d:
            self.d[total] = 0 
            
        self.d[total] += 1 
        
        return path
        