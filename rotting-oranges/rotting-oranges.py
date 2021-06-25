from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        res = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j)) 
                
                elif grid[i][j] == 1: 
                    visited.add((i,j))
        
        
        while q: 
            if not visited or len(visited) == 0: 
                return res
            
            size = len(q)
            res += 1 
            
            for _ in range(size):
                i, j = q.popleft() 
                
                for pair in dirs: 
                    r = i + pair[0]
                    c = j + pair[1]
                    
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r,c) in visited:
                        visited.remove((r,c))
                        grid[r][c] = -2
                        q.append((r,c))
        
        if visited: 
            return -1 
        
        return res