from collections import deque
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        self.diameter = 0
        
        for x,y in edges:
            if x not in graph:
                graph[x] = set()
            
            if y not in graph:
                graph[y] = set()
            
            graph[x].add(y)
            graph[y].add(x)     # because its an undirected edge, so add both. 
        
        
        self.dfs(graph, 0, set())
        
        return self.diameter
    
    def dfs(self, graph, currNode, visited):
        # base case 
        
        # logic 
        visited.add(currNode)
        d1, d2 = 0, 0
        dist = 0 
        for node in graph[currNode]:
            if node not in visited:
                dist = 1 + self.dfs(graph, node, visited)
                
            if dist > d1 :
                d1, d2 = dist, d1
            
            elif dist > d2:
                d2 = dist
                
        
        self.diameter = max(self.diameter, d1 + d2)
            
        return d1 
               