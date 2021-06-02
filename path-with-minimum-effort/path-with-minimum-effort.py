import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [] 
        diff = [[float('inf') for _ in range(len(heights[0]))] for _ in range(len(heights))]
        visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        dirs = [[-1,0], [1,0], [0,-1],[0,1]]
        
        pq.append((0,0,0))
        diff[0][0] = 0 
        
        while pq:
            
            difference, i, j = heapq.heappop(pq)
            visited[i][j] = True 
            
            for pair in dirs:
                r = i + pair[0]
                c = j + pair[1]
                
                if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and visited[r][c] == False:
                    
                    currDiff = abs(heights[i][j] - heights[r][c])
                    maxDiff = max(diff[i][j], currDiff)
                    
                    if diff[r][c] > maxDiff: 
                        diff[r][c] = maxDiff
                        
                        heapq.heappush(pq, (maxDiff, r, c))
        
        
        return diff[-1][-1]
                    
                    
                    
            
            
        
        

        