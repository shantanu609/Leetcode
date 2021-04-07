import math
class Solution:
    def numSquares(self, n: int) -> int:
        row = int(math.sqrt(n))
        dp = [0 for _ in range(n+1)]
        
        for j in range(1,len(dp)):
            dp[j] = float('inf')
        
        
        square = [i * i for i in range(1, row+1)]
        
        for i in range(1, len(dp)):
            for j in range(0, len(square)):
                numSq = square[j]
                if i >= numSq:
                    dp[i] = min(1 + dp[i- numSq], dp[i])

        return dp[-1]