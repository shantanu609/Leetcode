class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {} 
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in d:
                return [d[diff]+1, i+1]
            
            d[numbers[i]] = i 
        
        return [-1,-1]