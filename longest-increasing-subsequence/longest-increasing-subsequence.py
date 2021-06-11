class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1 
        res = 1
        
        for i in range(1, len(nums)):
            maxVal = 0 
            
            for j in range(0, i):
                
                if nums[i] > nums[j]: 
                    maxVal = max(maxVal, dp[j])
                
            
            dp[i] = maxVal + 1 
            
            res = max(res, dp[i])
        
        return res
            