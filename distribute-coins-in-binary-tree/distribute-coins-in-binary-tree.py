# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        self.neededCoins = 0 
        self.dfsHelper(root)
        return self.neededCoins 
    
    def dfsHelper(self, root):
        # base case 
        if not root:
            return 0 
        
        # logic 
        left_subtree_need = self.dfsHelper(root.left)
        right_subtree_need = self.dfsHelper(root.right)
        
        self.neededCoins += abs(left_subtree_need) + abs(right_subtree_need)
        
        return root.val + left_subtree_need + right_subtree_need - 1 