class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) - 1 
        
        while left <= right:
            mid = (left + right) // 2
            
            #--------------------
            n1, n2 = 0, 0 
            if mid-1 < 0:
                n1 = float('-inf')
            else:
                n1 = nums[mid-1]
            
            if mid +1 == len(nums):
                n2 = float('-inf')
            else:
                n2 = nums[mid+1]
            #--------------------

            if nums[mid] < n1:
                right = mid - 1         # look at first half 
            
            elif nums[mid] < n2:        
                left = mid + 1          # look at second half
            
            else:
                return mid 
        
        return -1