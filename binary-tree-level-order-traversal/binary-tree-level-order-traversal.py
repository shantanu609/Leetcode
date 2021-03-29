# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [] 
        
        result = [] 
        q = deque()
        node = root
        q.append(node)
        
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            result.append(temp.copy())
        
        return result