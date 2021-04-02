class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            [ai, bi] indicates that you must take course bi first
             [1,0]
                    0 -> 1
             [[1,0],[0,1]]
                 0 -> 1 
                 1 -> 0
            
            [[0,1],[0,2],[1,3],[2,4],[3,5],[3,0],[4,5]]
               
               1: [0]               
               2: [0]            
               3: [1, 0]            
               4: [2, 0]         
               5: [3, 1, 0, 2]      
               0: [3, 1, 0]     <- i
                   j   
            
                [1,0]
        """
        
        d = {}
        for pair in prerequisites:
            a, b = pair 
            if b not in d:
                d[b] = set()
            
            d[b].add(a)
            
            if a in d: 
                for num in d[a]:
                    d[b].add(num)
        
        for parent, childs in d.items():
            for j in childs:
                
                if j in d: 
                    set_ = d[j]
                    if parent in set_:
                        return False 
                else:
                    continue 
        
        return True 
            
            