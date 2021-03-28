# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None 
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node:
            self.res.append(node.val)
            self.helper(node.left)
            self.helper(node.right)
            