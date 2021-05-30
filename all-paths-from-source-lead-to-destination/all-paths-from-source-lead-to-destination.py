class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {} 
        
        for x, y in edges:
            if x not in graph:
                graph[x] = set() 
            
            graph[x].add(y)
        
        visited = set()
        
        return self.dfs(graph, source, destination, visited)
    
    def dfs(self, graph, source, dest, visited):
        # base cases
        if dest in graph and graph[dest]:
            return False 
        
        if source not in graph:
            return source == dest 
        
        # Logic 
        for node in graph[source]:
            if node in visited or node == source:
                return False 
            
            visited.add(node)
            if not self.dfs(graph, node, dest, visited):
                return False 
            visited.remove(node)
        
        return True 
            