class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = {}
        for num in arr1:
            d[num] = 0 
        
        for num in arr2:
            if num not in d:
                continue 
            else:
                d[num] += 1 
        
        res = []
        for num in arr3:
            if num in d:
                if d[num] > 0:
                    res.append(num)
        
        return res
                