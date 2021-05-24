# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.res = []
        self.deleteHelper(root, False, to_delete)
        
        return self.res 
    
    def deleteHelper(self, root, parent, to_delete):
        # base case 
        if not root:
            return None 
        
        # logic 
        if root.val in to_delete:
            root.left = self.deleteHelper(root.left, False, to_delete)
            root.right = self.deleteHelper(root.right, False, to_delete)
            return None 
    
        else:
            if not parent:
                self.res.append(root)
            
            root.left = self.deleteHelper(root.left, True, to_delete)
            root.right = self.deleteHelper(root.right, True, to_delete)
            return root 
        