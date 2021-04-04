class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """  0  1. 2. 3. 4. 5. 6
            [1, 2, 1, 3, 5, 6, 7]
             l        m        h
          
        """
        left = 0 
        right = len(nums) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            n1, n2 = 0, 0 
            
            if mid-1 < 0:
                n1 = float('-inf')
            else:
                n1 = nums[mid-1]
            
            if mid +1 == len(nums):
                n2 = float('-inf')
            else:
                n2 = nums[mid+1]

            if nums[mid] < n1:
                right = mid - 1 
            
            elif nums[mid] < n2:
                left = mid + 1 
            
            else:
                return mid 
        
        return -1