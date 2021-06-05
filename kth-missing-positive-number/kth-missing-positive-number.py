class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d = {} 
        largest = float('-inf')
        for num in arr:
            if num not in d:
                d[num] = 0 
            d[num] += 1 
            largest = max(largest, num)        
        
        missing = 0 
        for num in range(1, largest + 1): 
            if k == 0:
                return missing 
            
            if num not in d: 
                missing = num
                k -= 1 
        
        if k > 0: 
            missing = largest 
            while k > 0: 
                missing += 1 
                k -= 1 
        
        return missing
            
        