class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
            [[3,3,1,1],
             [2,2,1,2],
             [1,1,1,2]]
        """
        for col in range(len(mat[0])):
            self.helper(mat, 0, col)
        
        for row in range(1, len(mat)):
            self.helper(mat, row, 0)
            
        return mat 

    def helper(self, mat, row, col):
        temp = []
        r, c = row, col
        
        while r < len(mat) and c < len(mat[0]):
            temp.append(mat[r][c])
            r += 1 
            c += 1 
        
        temp.sort()
        i = 0 
        r, c = row, col
        while r < len(mat) and c < len(mat[0]):
            mat[r][c] = temp[i]
            r += 1 
            c += 1 
            i += 1