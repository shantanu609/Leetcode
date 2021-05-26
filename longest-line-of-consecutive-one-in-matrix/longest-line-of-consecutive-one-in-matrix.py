class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        dp = [[[0,0,0,0] for _ in range(len(mat[0]) + 2)] for _ in range(len(mat) + 1)]

        
        result = 0 
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0]) - 1):
                
                if mat[i-1][j-1] == 0:
                    continue 
                
                # horizontal -- 0th index in the inner sub-array
                dp[i][j][0] = 1 + dp[i][j-1][0]
                
                # vertical -- 1st index in the inner sub-array 
                dp[i][j][1] = 1 + dp[i-1][j][1]
                
                # diagonal -- 2nd index in the inner sub-array
                dp[i][j][2] = 1 + dp[i-1][j-1][2]
                
                # anti-diagonal -- 3rd index in the inner sub-array 
                # print(dp[i], dp[i][j][3], dp[i+1][j+1][3])
                dp[i][j][3] = 1 + dp[i-1][j+1][3]
                
                # update the final result 
                result = max(result, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        
        
        return result 
                