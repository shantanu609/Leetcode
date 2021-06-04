from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        eventCity = 0
        self.res = 0
        isConnected = set()
        
        for a, b in connections: 
            graph[a].append((b, 1))
            graph[b].append((a, 0))
           
        isConnected.add(0)
        
        for node in range(n):
#             if node in isConnected: 
#                 continue 
            
            self.dfs(graph, isConnected, node)
        
        return self.res 
    
    def dfs(self, graph, isConnected, source):
        # base case 
        
        
        # logic 
        isConnected.add(source)
        
        for childNode, cost in graph[source]:
            if childNode not in isConnected: 
                self.res += cost
                self.dfs(graph, isConnected, childNode)
       
                
            
"""
graph = {
         0 : {1}
         1 : {3}
         2 : {3}
         4 : {0, 5}
}
            0 1 2 3 4 5
indegree = [1,1,0,0,0,1]
                
                0 1 2 3 4 5
isconneceted = [T T F T T F]
                  2 0 0 0 1

count = 3

Example 2 : 

graph = {
        1 : {0, 2}
        3 : {2, 4}
}
               0 1 2 3 4 
isConnected = [T T F F T]
               0 0 1 0 1
"""