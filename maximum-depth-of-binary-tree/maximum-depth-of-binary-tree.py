# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     def __repr__(self):
#         return '%d' % (self.val)
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level = 0 
        
        while q:
            size = len(q)
            level += 1 
            for _ in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
        return level