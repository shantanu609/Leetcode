class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
           1) O(n2)
           2) O(nlong)
           3) O(n) -- bit mani O(1)
           4) Hashmap -- freq count  O(n) 
        """
        d = {} 
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0 
            
            d[nums[i]] += 1 
        
        for k,v in d.items():
            if v >= 2:
                return True
        
        return False