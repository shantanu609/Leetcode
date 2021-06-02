"""  5                 val key
    [6]     u -> v  = [6 ,  5] 
    
    graph = {
                2 : {0, 1, 3, 4, 5}
    } 
    
    CEO = indx for -1
"""
from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # data structure initialization 
        graph = {} 
        visited = set() 
        indegree = [0] * n 
        totalTime = 0 
        q = deque()
        CEO = headID
        
        # create the graph 
        for employee in range(len(manager)): 
            manager_ = manager[employee]
            if manager_ == -1:
                continue 
                
            if manager_ not in graph: 
                graph[manager_] = set() 
            
            graph[manager_].add(employee)
            
            indegree[employee] += 1 
    
        # apply topological sort 
        # get the o degreee nodes 
        q.append((CEO, 0)) 

        while q:
            
            for _ in range(len(q)):
                currManager, time = q.popleft() 
                visited.add(currManager)
                totalTime = max(totalTime, time)
                
                if currManager in graph: 
                    for allHisSub in graph[currManager]: 
                        if allHisSub not in visited:

                            q.append((allHisSub, informTime[currManager] + time))
            
        
        return totalTime
            