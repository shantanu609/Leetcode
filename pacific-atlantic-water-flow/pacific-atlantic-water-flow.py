from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        vistied = set() 
        pacificQ = deque()
        atlanticQ = deque()
        output = [] 
        
        for row in range(len(heights)):
            pacificQ.append((row, 0))
            atlanticQ.append((row, len(heights[0]) - 1))
        
        for col in range(len(heights[0])):
            pacificQ.append((0, col))
            atlanticQ.append((len(heights) -1 , col))
        
        out1 = self.bfs(heights, atlanticQ)
        out2 = self.bfs(heights, pacificQ)

    
        return list(out1.intersection(out2))
        
    def bfs(self, heights, q):
        output = set()

        while q : 
            i, j = q.popleft()
            output.add((i, j))
            
            for x, y in [[1,0], [-1,0],[0,-1],[0,1]]: 
                r = i + x 
                c = j + y 
                
                if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                    continue 
                
                if (r,c) in output:
                    continue 
                
                if heights[r][c] < heights[i][j]:
                    continue 
    
                q.append((r,c))
        
        return output
            
        