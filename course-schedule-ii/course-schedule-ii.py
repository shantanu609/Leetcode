from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # data structures needed 
        graph = {i : set() for i in range(numCourses)}
        result = [] 
        indegree = [0] * numCourses
        q = deque() 
        
        for nextCourse, prevCourse in prerequisites:
            graph[prevCourse].add(nextCourse)
            indegree[nextCourse] += 1 
        
        # skim through the indegree array to see if we have parent nodes with 0 indegree
        # for our topological sort 
        for node in range(numCourses):
            if indegree[node] == 0: 
                q.append(node)
        
        
        # BFS approach to traverse level by level and fill in the result array 
        while q: 
            curr = q.popleft() 
            # add curr to result as our path in taking courses 
            result.append(curr)
            
            # check for its neighbouring nodes for next level order traversal
            for node in graph[curr]:
                indegree[node] -=1 
                
                if indegree[node] == 0:
                    q.append(node)
        
        # before returning result, check if we dont have any cycles? 
        for node in range(numCourses):
            if indegree[node] > 0:
                return [] 
        
        return result