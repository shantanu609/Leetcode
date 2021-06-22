# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = {} 
        node = root 
        
        arr = [] 
        self.inorder(root, arr)
        left, right = 0, len(arr) - 1
        
        while left < right: 
            sum_ = arr[left] + arr[right]
            if sum_ == k:
                return True 
            
            if sum_ < k:
                left += 1 
            
            else:
                right -= 1 
        
        return False 
    
    
    def inorder(self, node, arr):
        if node:
            self.inorder(node.left, arr)
            arr.append(node.val)
            self.inorder(node.right, arr)
            
"""
set = {}
"""