class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start, end = 0 , 0 
        result = nums[0]
        rSum = nums[0]
        
        # loop from 1 till the end 
        for i in range(1, len(nums)):
            
            # check for the running sum for new nums[i]
            if nums[i] > rSum + nums[i]:
                start = i 
            rSum = max(rSum + nums[i], nums[i])
            
            # update the result to store the maximum running sum 
            if rSum > result:
                end = i 
            result = max(result, rSum)
        
        print(start, end)
        print(nums[start: end+1])
        
        return result 