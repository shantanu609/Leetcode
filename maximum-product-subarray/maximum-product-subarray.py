class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
                [-2, 3, 4]
                
                2 x 3 = 2, 3 , 6 x -3 = 6, -18
                    
                [-2,1,-4] = 8
                 -2 1, -4 = 1
        """
        imin = nums[0]
        imax = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            temp = min(nums[i], imin * nums[i], imax * nums[i])
            imax = max(nums[i], imin * nums[i], imax * nums[i])
            imin = temp
            res = max(res, imax)
        
        return res