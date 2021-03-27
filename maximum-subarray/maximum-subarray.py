class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        
        result = nums[0]
        rSum = nums[0]
        
        # loop from 1 till the end 
        for i in range(1, len(nums)):
            
            # check for the running sum for new nums[i]
            rSum = max(rSum + nums[i], nums[i])
            
            # update the result to store the maximum running sum 
            result = max(result, rSum)
        
        return result 