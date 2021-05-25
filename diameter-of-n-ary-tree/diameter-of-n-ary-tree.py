"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    res = None 
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root:
            return 0 
        
        self.res = 0 
        self.dfsHelper(root)
        return self.res 
    
    def dfsHelper(self, root):
        # base case 
        if not root:
            return 0 
        
        # logic 
        max_height1 = 0 
        max_height2 = 0 
        
        for childNode in root.children:
            parent_height = self.dfsHelper(childNode) + 1 
            
            if parent_height > max_height1:
                max_height1, max_height2 = parent_height, max_height1 
            
            elif parent_height > max_height2:
                max_height2 = parent_height 
            
        
        # get the total diameter
        total = max_height1 + max_height2 
        
        # update the result 
        self.res = max(self.res, total)
        
        # return max_height1 
        
        return max_height1
        
        
        
        
        
        
        
        