"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {} 
        p1 = head 
        p2 = dummy = Node(-1)
        
        while p1:
            p2.next = Node(p1.val)
            p2 = p2.next 
            d[p1] = p2 
            p1 = p1.next 
        
        p1 = head 
        
        while p1:
            newNode = d[p1]
            if p1.random:
                newNode.random = d[p1.random]
            p1 = p1.next 
        
        return dummy.next