class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue 
            else:
                return self.binarySearch(matrix[i], target)
        
        return False 

    def binarySearch(self, matrix, target):
        low = 0 
        high = len(matrix)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if matrix[mid] == target:
                return True 
            
            elif matrix[mid] < target:
                low = mid + 1 
            
            else:
                high = mid - 1
        
        return False 