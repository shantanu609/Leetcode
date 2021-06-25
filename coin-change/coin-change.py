class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for row in range(len(dp)):
            dp[row][0] = 0 
        
        for i in range(1, len(dp)):
            for amount in range(1, len(dp[0])):
                
                if amount >= coins[i-1]: 
                    dp[i][amount] = min(dp[i-1][amount], 1 + dp[i][amount -coins[i-1]])
                
                else:
                    dp[i][amount] = dp[i-1][amount]
        
        res = dp[-1][-1]
        
        if res == float('inf'):
            return -1 
    
        return res