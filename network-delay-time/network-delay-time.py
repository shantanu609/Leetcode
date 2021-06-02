from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        
        for u,v,w in times: 
            if u not in graph:
                graph[u] = []
            
            graph[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}
        visited = set() 
        dist[k] = 0 
        
        while True: 
            minNode = -1 
            minDist = float('inf')
            
            for node in range(1, n+1): 
                if node not in visited and dist[node] < minDist: 
                    minDist = dist[node]
                    minNode = node 
                
            if minNode == -1:
                break 
            
            if minNode in graph:
                for v, w in graph[minNode]:
                    dist[v] = min(dist[v], minDist + w)
            
            visited.add(minNode)
        
        res = max(dist.values())
        
        return res if res != float('inf') else -1 
        