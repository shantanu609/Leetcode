class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(min(len(matrix), len(matrix[0]))):
            # search in the row
            result1 = self._binarySearch(matrix, target, i, True)
            
            # search in the col 
            result2 = self._binarySearch(matrix, target, i, False)
            
            #check if any of the results could have found the target?
            if result1 or result2:
                return True 
        
        return False 
    
    def _binarySearch(self, matrix, target, i, vertical):
        
        left = 0 
        right = len(matrix) - 1 if vertical else len(matrix[0]) - 1 
    
        while left <= right:
            
            mid = (left + right) // 2 
            
            # check if we want to search in a row wise fashion or column wise?
            if vertical: 
                # column wise 
                
                if matrix[mid][i] == target:
                    return True 
                
                elif matrix[mid][i] < target:
                    left = mid + 1 
                
                else:
                    right = mid - 1 
                
            else:
                # row wise 
                
                if matrix[i][mid] == target:
                    return True 
            
                elif matrix[i][mid] < target:
                    left = mid + 1 
                
                else:
                    right = mid - 1 
                
        return False 
                