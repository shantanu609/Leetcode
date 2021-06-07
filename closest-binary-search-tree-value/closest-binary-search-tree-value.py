# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val 
        node = root 
        
        while node: 
            if abs(target - node.val) < abs(closest - target):
                closest = node.val

            if target < node.val:
                node = node.left 
                
            else:
                node = node.right 
    
    
        return closest