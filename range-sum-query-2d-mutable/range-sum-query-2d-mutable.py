class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix        

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]
        
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)