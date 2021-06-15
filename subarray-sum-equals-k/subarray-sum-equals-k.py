from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        rSum = 0 
        res = 0 
        
        for num in nums:
            
            rSum += num 
            
            # Situation 1: if running sum == target 
            if rSum == k:
                res += 1 
            
            # Situation 2: if running sum - target in hashmap 
            res += d[rSum - k]
            
            d[rSum] += 1 
    
        return res
        