class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 0:
            return 0 
        
        dp = [None] * (len(nums) + 1)
        dp[-1] = 0
        dp[-2] = nums[-1]
        
        for i in range(len(dp)-3, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        
        return dp[0]
