# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None 
        
        return self.deleteHelper(root, key)
    
    def deleteHelper(self, root, target):
        # base case 
        if not root:
            return None 
        
        # logic 
        if target > root.val:
            # search in right sub tree 
            root.right = self.deleteHelper(root.right, target)
        
        elif target < root.val:
            root.left = self.deleteHelper(root.left, target)
        
        else:
            # key found. 
            
            if not root.left:
                return root.right 
        
            # search for largest number from the left sub tree 
            node = root.left 
            
            while node and node.right:
                node = node.right 
            
            root.val = node.val 
            
            root.left = self.deleteHelper(root.left, node.val)
        
        return root