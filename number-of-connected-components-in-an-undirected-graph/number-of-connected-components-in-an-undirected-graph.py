class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {} 
        
        for a, b in edges:
            if a not in graph:
                graph[a] = set()
            
            if b not in graph:
                graph[b] = set() 
            
            graph[a].add(b)
            graph[b].add(a)
            
        count = 0 
        visited = set() 
        for node in range(n):
            if node not in visited: 
                count += 1 
                self.dfs(graph, node, visited)
        
        return count 
    
    def dfs(self, graph, source, visited):
        # base case 
        if source in visited:
            return 
        
        # logic 
        visited.add(source)
        if source in graph:
            for nextNode in graph[source]:
                self.dfs(graph, nextNode, visited)

            