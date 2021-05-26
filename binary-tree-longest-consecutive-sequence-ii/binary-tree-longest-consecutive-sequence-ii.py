# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0 
        self.res = 0 
        self.dfsHelper(root)

        return self.res 
    
    def dfsHelper(self, root):
        # base case 
        if not root:
            return (0, 0)
        
        # logic 
        inc, dec = 1, 1
        
        linc, ldec = self.dfsHelper(root.left)
        
        rinc, rdec = self.dfsHelper(root.right)
        
        if root.left and root.left.val == root.val + 1:
            # large/greater value on the left than the root node
            linc += 1 
            inc = max(inc, linc)
        
        if root.left and root.left.val == root.val - 1:
            # smaller value on the left --> value decremented 
            ldec += 1
            dec = max(dec, ldec)
            
        if root.right and root.right.val == root.val + 1:
            # large/greater value on the right --> value incremented 
            rinc += 1 
            inc = max(inc, rinc)
        
        if root.right and root.right.val == root.val - 1:
            # smaller valu on the right --> value decremented 
            rdec += 1 
            dec = max(dec, rdec)
            
        self.res = max(self.res, inc + dec - 1)
        
        return (inc, dec)