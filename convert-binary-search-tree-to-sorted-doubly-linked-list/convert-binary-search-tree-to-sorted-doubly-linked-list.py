"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
"""
    pred = left pointer
    succ = right pointer
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        stack = []
        node = root 
        head = tail = None
        
        while node or stack:
            # traverse on left 
            while node:
                stack.append(node)
                node = node.left 
                
            curr = stack.pop()
            if curr.right:
                node = curr.right
                
            if head is None:
                head = curr 
            if tail is None:
                tail = curr
            else:
                tail.right = curr 
                curr.left = tail 
                tail = tail.right 
        
        head.left = tail 
        tail.right = head 
        return head 
            
            