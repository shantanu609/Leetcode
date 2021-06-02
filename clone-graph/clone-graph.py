"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.d = {} 
        return self.dfs(node)
    
    def dfs(self, node):
        # base case 
        if not node:
            return node
        
        if node in self.d:
            return self.d[node]
        
        # Logic 
        newNode = Node(node.val, [])
        
        self.d[node] = newNode
        
        if node.neighbors: 
            for childNodes in node.neighbors:
                newNode.neighbors.append(self.dfs(childNodes))
        
        return newNode