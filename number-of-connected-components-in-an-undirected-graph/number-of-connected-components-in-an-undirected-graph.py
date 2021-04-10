class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0] * n 
        count = 0
        
        """
            0: {1}
            1 : {0, 2}
            2 : {1}
            3: {4}
            4 : {3}
        """
        d = {} 
        for edge in edges:
            one, two = edge 
            if one not in d:
                d[one] = [] 
            
            d[one].append(two)
            
            if two not in d:
                d[two] = [] 
            
            d[two].append(one)
        
        for i in range(n):
            if i not in d:
                d[i] = []
        
        visited = [0] * n 
        for node, edgesList in d.items():
            if visited[node] == 0:
                visited[node] = 1 
                self.dfs(visited, edgesList, d)
                count += 1 
        
        return count 
    
    def dfs(self, visited, edgesList, d):
        for node in edgesList:
            if visited[node] == 0 :
                visited[node] = 1 
                self.dfs(visited, d[node], d)