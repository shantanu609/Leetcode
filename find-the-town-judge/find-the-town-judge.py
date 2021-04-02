class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        indegree = [0] * N 
        outdegree = [0] * N
        
        for i in range(len(trust)):
            a,b = trust[i]
            indegree[b-1] += 1 
            outdegree[a-1] +=1 
        
        for i in range(N):
            if indegree[i] == N-1 and outdegree[i] == 0:
                return i+1
        
        return -1 