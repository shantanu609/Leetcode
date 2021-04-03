class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        while low < high:
            
            mid = (high + low) // 2 
            
            totalCount = self.getCount(matrix, mid)
            
            if totalCount < k:
                low = mid + 1
            
            else:
                high = mid 
        
        return low 
    
    def getCount(self, matrix, mid):
        length = len(matrix)-1 
        count = 0 
        
        for i in range(len(matrix)):
            
            j = length 
            
            while j >= 0 and matrix[i][j] > mid:
                j -= 1 
            
            count += j+1 
            
        return count 
            