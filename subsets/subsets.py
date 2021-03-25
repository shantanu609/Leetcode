class Solution:
    dirs = None 
    result = None
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(nums, set(), 0)
        return self.result 

    def backtrack(self, nums, subset, indx):
        # base case 
        self.result.append(subset.copy())
        if indx == len(nums):
            return 
        
        # logic 
        for i in range(indx, len(nums)):
            #action
            subset.add(nums[i])
            
            # recurse
            self.backtrack(nums, subset, i+1)
            
            # backtrack
            subset.remove(nums[i])