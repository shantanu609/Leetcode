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
            return 
        
        p1 = root 
        while p1: 
            temp = p1 
            p2 = p1.left 
            
            while p1 and p2:
                if p2 == p1.left:
                    p2.next = p1.right 
                    p2 = p2.next 
                else:
                    if p2 == p1.right:
                        if p1.next:
                            p2.next = p1.next.left 
                            p2 = p2.next 
                    p1 = p1.next 
            
            p1 = temp 
            p1 = p1.left 
        
        return root
                        