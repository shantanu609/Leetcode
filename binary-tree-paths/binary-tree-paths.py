# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None 
        
        self.res = [] 
        self.dfsHelper(root, [str(root.val)])
        return self.res 
    
    def dfsHelper(self, root, temp):
        # base case 
        if not root.left and not root.right:
            self.res.append(''.join(temp))
            return
        
        # logic 
        if root.left:
            temp.append('->')
            temp.append(str(root.left.val))
            self.dfsHelper(root.left, temp)
            temp.pop()
            temp.pop()
            
        if root.right:
            temp.append('->')
            temp.append(str(root.right.val))
            self.dfsHelper(root.right, temp)
            temp.pop()
            temp.pop()