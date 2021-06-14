class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort() 
        res = 0 
        
        for houseNum in houses: 
            indx = self.binarySearch(heaters, houseNum)
            
            if indx == len(heaters):
                res = max(res, houseNum - heaters[-1])
            
            elif indx == 0: 
                res = max(res, heaters[0] - houseNum)
            
            else:
                 res = max(res, min(heaters[indx] - houseNum, houseNum - heaters[indx-1]))
            
        
        return res 
    
    
    def binarySearch(self, heaters, target):
        left, right = 0, len(heaters) - 1
        
        while left <= right: 
            mid = (left + right) // 2 
            
            if heaters[mid] < target:
                left = mid + 1 
            
            else:
                right = mid - 1 
        
        return left