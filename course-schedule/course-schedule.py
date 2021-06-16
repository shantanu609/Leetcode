from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DS 
        graph = {} 
        indegree = [0 for _ in range(numCourses)]
        q = deque()
        
        for nextCourse, prevCourse in prerequisites:
            if prevCourse not in graph: 
                graph[prevCourse] = set()
                
            graph[prevCourse].add(nextCourse)
            
            indegree[nextCourse] += 1 
        
        for node in range(len(indegree)):
            if indegree[node] == 0:
                q.append(node)
            
        
        while q: 
            size = len(q)
            for _ in range(size):
                
                node = q.popleft() 
                
                if node in graph: 
                    for childNodes in graph[node]:
                        
                        indegree[childNodes] -= 1 
                        
                        if indegree[childNodes] == 0:
                            q.append(childNodes)
        
        for node in indegree:
            if node > 0:
                return False 
        
        return True

"""
4 - 1 - 3
  \ 2 /
"""
            
            