class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps = 0 
        farthest = 0 
        nextJump = 0 
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if i == nextJump: 
                nextJump = farthest 
                totalJumps += 1 
        
        return totalJumps