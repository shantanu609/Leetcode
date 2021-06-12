class Solution:
    def numSquares(self, n: int) -> int:
        sq = [i*i for i in range(int(n ** (1/2)) + 1)]
        
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0 
        
        for i in range(1, n+1):
            for square in sq: 
                
                if square > i : 
                    break
        
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[-1]
                
        
                

"""
Example : 12
num = [1, 4, 9] 
"""