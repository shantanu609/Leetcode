class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        startIndx, endIndx = 0, 0 
        i, j = 0, 1
        maxSum = nums[0]
        rSum = nums[0]
        
        while j < len(nums):            # expanding the window for maximum sum 
            rSum = rSum + nums[j]
            
            # check if we have a maxSum 
            maxSum = max(maxSum, nums[j], rSum)
            
            # check for ith pointer, if it should be incremented or not. 
            if nums[j] > rSum:
                i = j 
                rSum = nums[j]
            
            j += 1 
        
        return maxSum
        