# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True 
        
        leftHeight = self.getHeight(root.left, 0)
        rightHeight = self.getHeight(root.right, 0)
        
        if abs(leftHeight - rightHeight) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        else:
            return False 
        
    def getHeight(self, root, height):
        # base case 
        if not root:
            return height
        
        # logic 
        left_height = self.getHeight(root.left, height + 1)
        right_height = self.getHeight(root.right, height + 1)
        return max(left_height, right_height)