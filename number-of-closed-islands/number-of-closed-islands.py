class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0]) - 1) and grid[i][j] == 0:
                    self.dfs(grid, i, j)
        
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    res += 1 
        
        return res 
    
    def dfs(self, grid, i, j):
        # base case 
        
        
        # logic 
        dirs = [[0, -1], [-1, 0], [0, 1], [1,0]]
        grid[i][j] = 1 
        for pair in dirs: 
            r = pair[0] + i 
            c = pair[1] + j 
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                self.dfs(grid, r, c)
            