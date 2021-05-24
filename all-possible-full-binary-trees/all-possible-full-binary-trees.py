# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = None
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        
        self.memo = {0 : [], 1 : [TreeNode(0)]}
        
        self.recurseHelper(n)
        
        return self.memo[n]
    
    def recurseHelper(self, n):
        
        if n not in self.memo:
            result = [] 
            
            for x in range(n):
                y = n - 1 - x 
                
                for left in self.recurseHelper(x):
                    for right in self.recurseHelper(y):
                        
                        newNode = TreeNode(0)
                        newNode.left = left 
                        newNode.right = right 
                        result.append(newNode)
                        
            self.memo[n] = result 
        
        return self.memo[n]