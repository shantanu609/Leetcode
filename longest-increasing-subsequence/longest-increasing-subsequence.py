class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1 
        res = 1
        
        for i in range(1, len(nums)):
            temp = 0 
            
            for j in range(0, i):
                
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j])
            
            dp[i] = temp + 1 
            
            res = max(res, dp[i])
        
        
        return res