class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums)-1 
        
        k_smallest = len(nums) - k 
        while low <= high:
            res = self.partition(low, high, nums)
            print(res)
            if res == k_smallest:
                return nums[res]

            elif res < k_smallest:
                low = res + 1 

            else:
                high = res - 1 
        
        return res
        
    def partition(self, start, end, nums):
        pivot = start
        
        while start <= end:
            
            while start <= end and nums[start] <= nums[pivot]:
                start += 1 
            
            while start <= end and nums[pivot] <= nums[end]:
                end -= 1 
            
            if start > end:
                break 
            
            nums[start], nums[end] = nums[end], nums[start]
            
            start += 1 
            
        nums[pivot], nums[end] = nums[end], nums[pivot]
        return end 