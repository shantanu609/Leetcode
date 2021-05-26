# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.helper(preorder)
    
    def helper(self, preorder):
        # base case 
        if len(preorder) == 0:
            return None
        
        # logic 
        root = TreeNode(preorder[0])
        indx = 1
        while indx < len(preorder) and preorder[0] > preorder[indx]:
            indx += 1 

        root.left = self.helper(preorder[1: indx])
        root.right = self.helper(preorder[indx: ])
        
        return root
        