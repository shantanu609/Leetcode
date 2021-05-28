class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]  * len(nums)
        left = 0 
        right = len(nums) - 1 
        
        for i in range(len(nums)-1, -1, -1):
            sq = None 
            if abs(nums[left]) < abs(nums[right]):
                sq = nums[right]
                right -= 1 
            
            else:
                sq = nums[left]
                left += 1 
            
            res[i] = sq ** 2
        
        return res