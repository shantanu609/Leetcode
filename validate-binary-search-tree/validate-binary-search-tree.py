# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    storeValues = None 
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True 
        self.storeValues = [] 
        self.inorderHelper(root)
        for i in range(1, len(self.storeValues)):
            if self.storeValues[i] <= self.storeValues[i-1]:
                return False 
        
        return True 
    
    def inorderHelper(self, root):
        if root:
            self.inorderHelper(root.left)
            self.storeValues.append(root.val)
            self.inorderHelper(root.right)
        