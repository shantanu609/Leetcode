from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: set() for i in range(1, n+1)} 
        indegree = [0] * (n+1)
        q = deque() 
        
        for previousCourse, nextCourse in relations: 
            graph[previousCourse].add(nextCourse)
            
            indegree[nextCourse] += 1 
        
        for node in graph.keys():
            if indegree[node] == 0:
                q.append(node)

        miniSemester = 0 
        count = 0 
        
        while q: 
            
            miniSemester += 1 
            nextQ = deque() 
            
            for node in q: 
                count += 1 
                if node in graph:
                    for eachNode in graph[node]:  
                        indegree[eachNode] -= 1 
                        if indegree[eachNode] == 0:
                            nextQ.append(eachNode)
            
            q = nextQ 
            
        print(miniSemester, count)
        
        return miniSemester if count == n else -1