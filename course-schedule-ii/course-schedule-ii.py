from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        d = {}
        indegree = [0 for _ in range(numCourses)]
        for pair in prerequisites:
            c1, c2 = pair 
            indegree[c1] += 1 
            
            if c2 not in d:
                d[c2] = [] 
            
            d[c2].append(c1)
        
        q = deque()
        for node in range(len(indegree)):
            if indegree[node] == 0:
                q.append(node)
            
        res = []         
        while q:
            curr = q.popleft()
            res.append(curr)
            
            if curr in d:
                for neigh in d[curr]:
                    indegree[neigh] -= 1 
                    
                    if indegree[neigh] == 0:
                        q.append(neigh)
        
        for degree in indegree:
            if degree > 0:
                return [] 
        return res