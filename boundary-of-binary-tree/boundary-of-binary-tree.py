# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return [] 
        res = [] 
        if not self.isLeaf(root):
            res.append(root.val)
        
        node = root.left 
        
        while node:
            if not self.isLeaf(node):
                res.append(node.val)
            
            if node.left:
                node = node.left 
            
            else:
                node = node.right
            
        self.addLeafHelper(root, res)
        
        # last part is adding the right view 
        stack = []
        node = root.right 
        
        while node:
            if not self.isLeaf(node):
                stack.append(node.val)
            
            if node.right:
                node = node.right
            
            else:
                node = node.left 
        
        while stack:
            res.append(stack.pop())
        
        return res
        
        
    def isLeaf(self, node):
        if not node.left and not node.right:
            return True 
        
        return False 
    
    
    def addLeafHelper(self, node, res):
        # base case 
        if not node:
            return 
        
        # logic 
        if self.isLeaf(node):
            res.append(node.val)
        
        if node.left:
            self.addLeafHelper(node.left, res)
        
        if node.right:
            self.addLeafHelper(node.right, res)