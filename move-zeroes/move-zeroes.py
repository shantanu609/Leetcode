class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0 
        for i in range(len(nums)):
            nums[i], nums[p1] = nums[p1], nums[i]
            if nums[p1] != 0:
                p1 += 1 
        
        