# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = None 
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.res = [] 
        self.helper(root)
        for i in range(len(self.res)):
            node = self.res[i]
            if node == p:
                if i+1 < len(self.res):
                    return self.res[i+1]
                else:
                    break 
        
        return None 
    
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.res.append(root)
            self.helper(root.right)