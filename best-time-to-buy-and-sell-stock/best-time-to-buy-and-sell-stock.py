class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            [7,1,5,4,6,4]
                       i
             
             min = 1
             max = 6
             profit = max - min = 5
             max = min(max, profit) = min(0, 1) = 5
         """
        minCost = float('inf')
        profit = 0 
        
        for i in range(len(prices)):
            if prices[i] < minCost:
                # buy it 
                minCost = prices[i]
            else:
                # sell 
                profit = max(profit, prices[i] - minCost)
        
        return profit 