class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        
        total = 0 
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                
                if matrix[i-1][j-1] == 0:
                    continue 
                
                # check if the cell forms up a square
                isSquare = True if (dp[i-1][j-1] > 0 and dp[i-1][j] > 0 and dp[i][j-1] > 0) else False 
                
                if isSquare:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 
                
                else:
                    dp[i][j] = 1 
                
                
                total += dp[i][j]
    
        
        return total