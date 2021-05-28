class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
        
        return self.res 
    
    def dfs(self, grid, i, j):
        # base case
        
        
        # logic 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        grid[i][j] = -2 
        self.res += self._getTotalSides(grid, i, j)
        for pair in dirs:
            r = pair[0] + i 
            c = pair[1] + j 
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[i][j] == 1:
                self.dfs(grid, r, c)
        
    
    def _getTotalSides(self, grid, i, j):
        count = 4 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for pair in dirs:
            r = i + pair[0]
            c = j + pair[1]
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (grid[r][c] == 1 or grid[r][c] == -2):
                count -= 1 
        
        return count