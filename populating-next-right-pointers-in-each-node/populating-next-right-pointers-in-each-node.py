"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root 
        
        node = root 
        while node: 
            curr = node 
            child = node.left 
            
            while curr and child: 
                if curr.left == child: 
                    child.next = curr.right 
                    child = child.next 
                
                else: 
                    if not curr.next: 
                        break 
                    
                    if curr.right == child: 
                        child.next = curr.next.left 
                        child = child.next 
                    
                    else:
                        curr = curr.next 
            
            node = node.left 
    
        return root 