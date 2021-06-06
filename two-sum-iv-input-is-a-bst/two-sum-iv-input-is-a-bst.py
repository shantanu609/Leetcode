# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = {} 
        node = root 
        stack = [] 
        
        while node or stack:
            while node:
                stack.append(node)
                if k - node.val in d:
                    return True 
                
                d[node.val] = node 
                node = node.left
            
            curr = stack.pop() 
            node = curr.right 
        
        return False
            
            
            
            