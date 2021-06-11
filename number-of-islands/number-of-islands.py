class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == "1":
                    self.dfs(grid, i , j)
                    num += 1 
        
        return num 
    
    def dfs(self, grid, i, j):
        # base case 
        
        
        # Logic 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        grid[i][j] = '-2'
        
        for pair in dirs: 
            r = i + pair[0]
            c = j + pair[1]
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                self.dfs(grid, r, c)
        