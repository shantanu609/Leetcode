class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high  = matrix[n-1][n-1]
        
        while low < high:
            
            mid = (low + high) // 2
            
            tempLow, tempHigh = matrix[0][0], matrix[n-1][n-1]
            
            count, tempLow, tempHigh = self.binaryHelper(matrix, mid, tempLow, tempHigh)
            
            if count == k:
                return tempLow 
        
            elif count < k:
                low = tempHigh 
            
            else:
                high = tempLow 
            
        
        return low 
    
    
    def binaryHelper(self, matrix, mid, tempLow, tempHigh):
        row = len(matrix) - 1
        col = 0 
        count = 0 
        
        # operation is to count the number of elements less than equals to mid 
        while row >= 0 and col < len(matrix[0]):
            
            if matrix[row][col] > mid:
                # adjust high. Bring it closer to mid 
                tempHigh = min(tempHigh, matrix[row][col])
                row -= 1 
            
            else:
                # shift low, bring it forward towards mid 
                tempLow = max(tempLow, matrix[row][col])
                col += 1 
                count += row + 1 
        
        return (count, tempLow, tempHigh)