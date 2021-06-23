class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        imin = float('inf')
        
        for price in prices: 
            imin = min(imin, price)
            profit  = max(profit, price - imin)
        
        return profit