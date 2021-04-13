class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i 
            
            else:
                last = d[nums[i]]
                if abs(last - i) <= k:
                    return True 
                d[nums[i]] = i
        return False 