class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            1) BF - > 2-D array
            2) BF apto. -> 1-D -> sort -> search/ bs
            3) 
        """
        row = len(matrix)-1
        col = 0 
        
        while row >= 0 and col < len(matrix[0]):
            num = matrix[row][col]
            
            if num == target:
                return True 
            
            elif num < target: 
                col += 1 
            
            else:
                row -= 1 
        
        return False 