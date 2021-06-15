# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None 
        
        self.arr = [] 
        self.inorder(root)
        
        for i in range(len(self.arr) - 1):
            if self.arr[i].val == p.val: 
                return self.arr[i+1]
        
        return None 
    
    def inorder(self, root):
        # base case 
        
        
        # logic 
        if root:
            self.inorder(root.left)
            self.arr.append(root)
            self.inorder(root.right)
            