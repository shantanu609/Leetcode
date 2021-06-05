class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_to_right = [0] * len(prices)
        right_to_left = [0] * (len(prices) + 1)
        profit = 0 
        min_ = prices[0]
        
        for i in range(1, len(prices)):
            left_to_right[i]  = max(left_to_right[i-1], prices[i] - min_)
            
            min_ = min(min_, prices[i])
        
        max_ = prices[-1]

        for i in range(len(prices)-1, -1, -1):
            right_to_left[i] = max(right_to_left[i+1], max_ - prices[i])
            
            max_ = max(max_, prices[i])
        
        for i in range(len(prices)):
            profit = max(profit, left_to_right[i] + right_to_left[i+1])
        
        return profit