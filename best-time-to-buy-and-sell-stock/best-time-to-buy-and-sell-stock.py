class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        profit = 0 
        
        for i in range(len(prices)):
            price = prices[i]
            
            min_ = min(price, min_)
            profit = max(profit, price - min_)
        
        return profit
        
        