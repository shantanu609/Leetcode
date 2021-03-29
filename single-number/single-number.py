class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            0100
            0001
            0101
            00
        """
        res = 0 
        for num in nums:
            res = res ^ num 
        
        return res
            