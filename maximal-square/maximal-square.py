class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        side = 0 
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1  + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                
                    side = max(side, dp[i][j])
                
        area = side * side 
        
        return area