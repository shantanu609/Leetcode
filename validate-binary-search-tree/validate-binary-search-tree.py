# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        arr = [] 
        self._inorder(root, arr)
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False 
        
        return True
    
    def _inorder(self, root, arr):
        if root:
            arr = self._inorder(root.left, arr)
            arr.append(root.val)
            arr = self._inorder(root.right, arr)
        
        return arr