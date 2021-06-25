class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {} 
        right = {} 
        count = {} 
        ans = len(nums)
        
        for i in range(len(nums)): 
            if nums[i] not in left: 
                left[nums[i]] = i
                
            right[nums[i]] = i 
            
            if nums[i] not in count:
                count[nums[i]] = 0 
                
            count[nums[i]] += 1 
        
        degree = max(count.values())
        for num in count:
            if count[num] == degree: 
                ans = min(ans, right[num] - left[num] + 1)
        
        return ans