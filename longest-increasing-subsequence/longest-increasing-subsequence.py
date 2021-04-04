class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """              j       
           [10,9,2,5,3,7,101,18]
                             i   
           [1, 1,1,2,2,3, 4, 4]
           maxans = 4
           temp = 0
        """
        dp = [0] * len(nums)
        dp[0] = 1 
        result = 1
        
        for i in range(1, len(nums)):
            runningMax = 0 
            
            # come from back till i 
            for j in range(0, i):
                
                # if any number at j is smaller, we got a max value 
                if nums[i] > nums[j]:
                    runningMax = max(runningMax, dp[j])
            
            # increase the runnigMax by 1. 
            dp[i] = runningMax + 1 
            result = max(result, dp[i])
        
        return result 