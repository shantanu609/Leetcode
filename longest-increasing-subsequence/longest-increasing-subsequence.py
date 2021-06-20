class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = 1 
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            res = max(res, dp[i]) 
        
        return res
                

"""
        [10,9,2,5,3,7,101,18]
         
         [2,3,7,101]
         [2,3,7,18]
         
"""