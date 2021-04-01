class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {} 
        for i in range(len(nums1)):
            if nums1[i] not in d:
                d[nums1[i]] = 0 
            
            d[nums1[i]] += 1 
        
        res = []
        
        for i in range(len(nums2)):
            if nums2[i] in d:
                d[nums2[i]] -= 1 
                if d[nums2[i]] <= 0:
                    d.pop(nums2[i])
                res.append(nums2[i])
        
        return res