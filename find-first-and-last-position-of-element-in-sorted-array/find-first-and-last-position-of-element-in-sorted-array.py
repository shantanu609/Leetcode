class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        
        res = [] 
        if nums[0] == target:
            res.append(0)
        last = 0
        
        for i in range(0, len(nums)-1):
            if nums[i+1] == target:
                last = i+1
            
                if len(res) == 0:
                    res.append(last)
        
        res.append(last)
        
        if len(res) <= 1 :
            return [-1,-1]
        
        return res
        
                