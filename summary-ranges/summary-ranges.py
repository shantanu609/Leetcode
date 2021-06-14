class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = [] 
        i = 0 
        while i < len(nums):
            j = i
            last = nums[i]
            
            while j+1 < len(nums) and nums[j] + 1 == nums[j+1]:
                j += 1 
            
            if i == j:
                res.append(str(nums[j]))
            
            else:
                res.append(str(nums[i]) + '->' + str(nums[j]))
            
            i = j + 1 
            
        return res