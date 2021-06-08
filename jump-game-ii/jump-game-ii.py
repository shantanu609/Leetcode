class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 
        currJumpEnd = 0 
        farthest = 0 
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == currJumpEnd:
                currJumpEnd = farthest 
                jumps += 1 
        
        return jumps