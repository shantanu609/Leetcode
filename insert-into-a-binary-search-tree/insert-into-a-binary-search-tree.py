# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        node = root 
        
        while node:
            if node.val < val:
                # go to right sub tree 
                if node.right is None:
                    node.right = TreeNode(val)
                    return root 
                
                node = node.right
            
            elif node.val > val:
                # go to left sub tree
                if node.left is None:
                    node.left = TreeNode(val)
                    return root 
                node = node.left 
        
        return root