# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None 
        
        return self.searchHelper(root, val)
    
    def searchHelper(self, root, target):
        # base case 
        if not root:
            return None 
        
        # logic
        if root.val == target:
            return root 
        
        if root.val < target: 
            # search in right half 
            return self.searchHelper(root.right, target)
        
        else:
            # search in left half 
            return self.searchHelper(root.left, target)