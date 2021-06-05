class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums1:
            if num not in d:
                d[num] = 0 
            
            d[num] += 1 
        
        output = [] 
        
        for num in nums2:
            if num in d: 
                output.append(num) 
                
                d[num] -= 1 
                if d[num] == 0:
                    d.pop(num)
        
        return output