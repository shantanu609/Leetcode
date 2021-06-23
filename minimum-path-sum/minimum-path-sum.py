class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                
                if i == len(grid)-1 and j != len(grid[0])-1: 
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                    continue 
                
                if i != len(grid)-1 and j == len(grid[0])-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                    continue 
                
                if i != len(grid)-1 and j != len(grid[0])-1: 
                    dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
                    continue
                
                dp[i][j] = grid[i][j]
        
        return dp[0][0]
                
                 