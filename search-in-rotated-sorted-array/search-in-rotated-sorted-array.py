class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 
        
        while left <= right: 
            
            mid = (left + right) // 2 
            
            if nums[mid] == target:
                return mid 
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target  and target < nums[mid]: 
                    right = mid - 1 
                
                else:
                    left = mid + 1 
            
            else:
                if nums[mid] < target and target <= nums[right]: 
                    left = mid + 1 
                
                else:
                    right = mid - 1 
        
        return -1
     
"""          lr
    [4,5,6,7,0,1,2]
             m      
             
     l  r        
    [3, 1]
     m
    
    if nums[low] < nums[mid] : 
        if target >= nums[low] and target < nums[mid]: 
                high = mid - 1 
        else:
                low = mid + 1 
    
    else:
        if target > nums[mid] and target <= nums[high]: 
            low = mid + 1 
        
        else: 
            high = mid - 1 
            
    
"""