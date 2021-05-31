class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = {i : set() for i in range(len(graph))} 
        
        for i in range(len(graph)):
            for node in graph[i]: 
                d[i].add(node)
    
        self.res = [] 
        visited = set() 
        self.dfs(d, 0, len(graph)-1, visited, [0])
        return self.res 
    
    def dfs(self, graph, source, dest, visited, temp):
        # base case 
        if source == dest: 
            self.res.append(temp.copy())
            return 
        
        # logic 
        if source in graph: 
            for node in graph[source]:
                visited.add(node)
                temp.append(node)
                
                # recurse 
                self.dfs(graph, node, dest, visited, temp)
                
                # backtrack 
                visited.remove(node)
                temp.pop() 
        
        
        