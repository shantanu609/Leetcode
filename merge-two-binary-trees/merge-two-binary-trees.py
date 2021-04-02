# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.dfs(root1, root2)
    
    def dfs(self, node1 = None, node2 = None):
        if not node1 and not node2:
            return 
        a , b = 0 , 0 
        if node1 :
            a = node1.val 
        if node2:
            b = node2.val 
        
        root = TreeNode(a+b)
        temp1, temp2 = None, None 
        if node1 and node1.left:
            temp1 = node1.left
        if node2 and node2.left:
            temp2 = node2.left
        
        temp3, temp4 = None, None 
        if node1 and node1.right:
            temp3 = node1.right
        if node2 and node2.right:
            temp4 = node2.right
        root.left = self.dfs(temp1, temp2)

        root.right = self.dfs(temp3, temp4)
        
        return root 
    
"""
    1           1
  2                2         
 3                    3
"""