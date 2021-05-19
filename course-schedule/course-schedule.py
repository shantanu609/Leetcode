from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outdegree = [0 for _ in range(numCourses)]
        d = {} 
        self._formGraph(outdegree, d, prerequisites)
        
        q = deque()
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                q.append(i)

        return self._check(q, outdegree, d)

    def _formGraph(self, outdegree, d, prereq):
        for pair in prereq:
            c1, c2 = pair 
            outdegree[c1] += 1 
            
            if c2 not in d:
                d[c2] = [] 
                
            d[c2].append(c1)
    
    def _check(self, q, outdegree, d):
        while q: 
            curr = q.popleft()
            if curr in d:
                for neigh in d[curr]:

                    outdegree[neigh] -= 1 
                    if outdegree[neigh] == 0:
                        q.append(neigh)

        for degree in outdegree:
            if degree > 0:
                return False 
        
        return True