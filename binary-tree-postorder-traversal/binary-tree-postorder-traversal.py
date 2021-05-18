# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = [] 
        self._helper(root, res)
        return res 
    
    def _helper(self, root, output):
        if root:
            self._helper(root.left, output)
            self._helper(root.right, output)
            output.append(root.val)