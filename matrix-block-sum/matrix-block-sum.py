class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
            mat = [[1,2,3],
                   [4,5,6],
                   [7,8,9]], k = 1
                   
            ans = [[12,21,16],
                   [27,45,33],
                   [24,39,28]]
        """
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                total = self.helper(mat, i, j, k)
                ans[i][j] = total
            
        return ans 
    
    def helper(self, mat, i, j, k):
        rMin = max(i - k, 0)
        rMax = min(i + k, len(mat)-1)
        
        cMin = max(j - k, 0)
        cMax = min(j + k, len(mat[0]) -1)
        
        total = 0
        for r in range(rMin, rMax + 1):
            for c in range(cMin, cMax + 1):
                total += mat[r][c]
        
        return total
                
        
