class Solution:
    result = None 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.result = [] 
        self.backtrack(nums, 0, set())
        return self.result 
    
    def backtrack(self, nums, indx, subset):
        self.result.append(subset.copy())
        
        # base case 
        if indx == len(nums):
            return 
        
        # logic 
        for i in range(indx, len(nums)):
            # action 
            subset.add(nums[i])
            
            # recurse
            self.backtrack(nums, i+1, subset)
            
            # backtrack
            subset.remove(nums[i])
            
# Time : O(2 ^ n)
# Space: O(n)