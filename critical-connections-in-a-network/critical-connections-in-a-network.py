class Solution:
    
    graph = None 
    mainEdgeDic = None 
    rank = None 
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
             0 -> 1 delete 
             target : start from node0 - > node1
             
             start = 3 and end node is 1
             res= [[3,1]]
             
         d = {    
                 0: [1, 2]
                 1 :[0, 2, 3]
                 2: [0,1]
                 3 :[]
            }
                     
            input = [[0,1],[1,2],[2,0],[1,3]]
            
            degree = [2,3,2,1]
        """
        self.graph = {} 
        self.mainEdgeDic = {} 
        self.rank = {}
        
        self.formGraph(n, connections)
        self.dfs(0, 0)
        
        result = []
        for k, v in self.mainEdgeDic.items():
            result.append(list(k))
        
        return result 
    
    def formGraph(self, n, connections):
        for i in range(n):
            self.rank[i] = None 
        
        for pair in connections:
            u,v = pair 
            if u not in self.graph:
                self.graph[u] = list()
            self.graph[u].append(v)
            
            if v not in self.graph:
                self.graph[v] = list()
            self.graph[v].append(u)
        
            self.mainEdgeDic[(min(u,v), max(u,v))] = 1 
    
    def dfs(self, node, rank):
        # base case 
        if self.rank[node]:
            return self.rank[node]
        
        # logic 
        self.rank[node] = rank 
        
        next_rank = rank + 1
        
        for neigh in self.graph[node]:
            
            # skip the parent 
            if self.rank[neigh] and self.rank[neigh] == rank - 1 :
                continue 
            
            # go deeper to find the cycle and come back up with the minimum rank 
            recRank = self.dfs(neigh, rank+1)
            
            if recRank <= rank:
                pair = (min(node, neigh), max(node, neigh))
                if pair in self.mainEdgeDic:
                    self.mainEdgeDic.pop(pair)
            
            next_rank = min(next_rank, recRank)
            
        return next_rank 