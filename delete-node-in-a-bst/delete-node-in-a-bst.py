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
        if root.val > target:
            # search in the left sub tree. 
            root.left = self.deleteHelper(root.left, target)
        
        elif root.val < target:
            # search in the right sub tree. 
            root.right = self.deleteHelper(root.right, target)
        
        else:
            # key found! 
            
            # 1) if no left sub tree to the target node, just return right sub tree. 
            if not root.left:
                return root.right 
            
            # 2) a)  else find the largest node value from the right side of the left subtree and replace. 
            curr = root 
            curr = root.left 
            while curr.right:
                curr = curr.right 
            
            root.val = curr.val 
            
            # 2) b) delete this new node, that we just replaced, present in curr 
            root.left = self.deleteHelper(root.left, curr.val)
        
        
        return root
            