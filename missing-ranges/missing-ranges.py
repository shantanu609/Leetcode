class Solution:
    res = None 
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        self.res = [] 
        
        # first edge case, if the nums array is empty 
        if len(nums) == 0:
            self.helper(lower, upper)
            return self.res
        
        # check for range between lower and first number in the array exclusive
        self.helper(lower, nums[0]-1)
        
        # check for ranges in the nums array 
        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i+1]) > 1 :
                self.helper(nums[i]+1, nums[i+1]-1)
        
        # check for range between last number in the array (exclusive) and upper limit 
        self.helper(nums[-1]+1, upper)
    
        # return result 
        return self.res
            
    
    def helper(self, lower, upper):
        if lower > upper:
            return 
        
        elif lower == upper:
            self.res.append(str(lower))
        
        else:
            self.res.append(str(lower) + '->' + str(upper))