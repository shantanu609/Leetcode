from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # data structure 
        q = deque()
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        steps = 0 
        
        # Step1) Find first island. 
        for i in range(len(grid)):
            found = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    self.dfs(grid, i, j, q)
                    found = True 
                    break
            
            if found: 
                break 
        
        while q: 
            size = len(q)
            
            for _ in range(size):
                i, j = q.popleft() 
                
                for pair in self.dirs: 
                    r = i + pair[0]
                    c = j + pair[1]
                    
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]): 
                        if grid[r][c] == 1:
                            # we found the second bridge 
                            return steps 
                    
                        if grid[r][c] == 2:
                            continue 
                        
                        grid[r][c] = 2 
                        q.append((r, c))
            steps += 1 
        
        return steps
        
    
    def dfs(self, grid, i, j, q):
        # base case 
        
        # logic 
        grid[i][j] = 2 
        q.append((i,j))
        for pair in self.dirs: 
            r = i + pair[0]
            c = j + pair[1]
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1: 
                self.dfs(grid, r, c, q)
