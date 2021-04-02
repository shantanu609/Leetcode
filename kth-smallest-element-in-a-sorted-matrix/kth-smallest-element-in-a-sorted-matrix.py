class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                temp.append(matrix[i][j])
        temp.sort()
        return temp[k-1]