class Solution:
    res = None 
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [] 
        
        self.res = []
        self.backtrack(nums, [])
        return self.res 
    
    def backtrack(self, nums, tempSet):
        # base case
        if len(tempSet) == len(nums):
            self.res.append(tempSet.copy())
            return 
        
        # Logic 
        for i in range(len(nums)):
            
            # action
            if nums[i] in tempSet:
                continue 
                
            tempSet.append(nums[i])

            # recurse
            self.backtrack(nums, tempSet)

            # backtrack
            tempSet.pop()                
            
"""
        [1, 2, 3]       set(1)
            i
         
         [1,2,3]        set(1)
              i
        
         [1,2,3]        set(1,3,2)
            i
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""