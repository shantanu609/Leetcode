from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0 
        
        # data structure initialization 
        weight = [[0 for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        q = deque()
        result = 0 
        
        # copy the matrix in the weights array 
        for i in range(1, len(weight)-1):
            for j in range(1, len(weight[0])-1):
                weight[i][j] = matrix[i-1][j-1]
            
        outdegree = [[0 for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]
        
        # Creating weighted routes for each cell similar to a graph 
        for i in range(1, len(weight)-1):
            for j in range(1, len(weight[0])-1):
                for pair in dirs: 
                    r = pair[0] + i
                    c = pair[1] + j
                    
                    # if 0 <= r < len(weight) and 0 <= c < len(weight[0]): 
                    if weight[i][j] < weight[r][c]:
                        outdegree[i][j] += 1 
        
        # check for 0 degree nodes to start our topological sort 
        for i in range(len(weight)):
            for j in range(len(weight[0])): 
                if outdegree[i][j] == 0:
                    q.append((i, j))
        
        # BFS traversal for getting the longest increasing route 
        while q : 
            size = len(q)
            result += 1
            
            for _ in range(size):
                i, j = q.popleft() 
                
                for pair in dirs: 
                    r = i + pair[0]
                    c = j + pair[1]
                    
                    if 0 <= r < len(weight) and 0 <= c < len(weight[0]):
                        if weight[i][j] > weight[r][c]:
                            outdegree[r][c] -=1 

                            if outdegree[r][c] == 0:
                                q.append((r, c))
        
        return result 