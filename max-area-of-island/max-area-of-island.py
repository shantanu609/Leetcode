class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = [0]
        self.dirs = [[1,0], [-1,0], [0, 1], [0, -1]]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    self.curr = 0 
                    self.dfs(grid, i, j, 0)
        
        # print(self.res)
        return max(self.res)
    
    def dfs(self, grid, i, j, currArea): 
        # base case 
        
        # logic 
        grid[i][j] = -2
        self.curr += 1 
        # self.res = max(currArea, self.res)

        for pair in self.dirs: 
            r = pair[0] + i 
            c = pair[1] + j 
            
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                self.dfs(grid, r, c, currArea)
        
        self.res.append(self.curr)

            
"""
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
     
     [1,1,0,0,0],
     [1,1,0,0,0],
     [0,0,0,1,1],
     [0,0,0,1,1]]
"""