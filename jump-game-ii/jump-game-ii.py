class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 0
        dp = [float('inf') for _ in range(len(nums))]
        dp[-1] = 0 
        
        for i in range(len(nums)-2, -1 ,-1):
            for j in range(1, nums[i]+1):
                if i + j >= len(nums):
                    break
                dp[i] = min(dp[i], 1 + dp[i+j])
        print(dp)
        return dp[0]
         
    
    """      0 1 2 3 4
            [2,3,1,1,4]
            [2,1,2,1,0]
             1 1 
             1 2
             -------
             2 3 
    """