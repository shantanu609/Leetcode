import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        pq = [] 
        # First column row wise 
        i = j = 0 
        
        while i < len(mat): 
            j = 0 
            row = i 
            
            while i < len(mat) and j < len(mat[0]): 
                heapq.heappush(pq, mat[i][j])
                i += 1 
                j += 1 
            
            i = row 
            j = 0 
            
            while j < len(mat[0]) and i < len(mat): 
                mat[i][j] = heapq.heappop(pq)
                i += 1 
                j += 1 
            
            i = row 
            i += 1 
    
        i = 0 
        j = 1 
        
        while j < len(mat[0]): 
            col = j 
            i = 0 
            
            while i < len(mat) and j < len(mat[0]): 
                heapq.heappush(pq, mat[i][j])
                i += 1 
                j += 1 
            
            i = 0 
            j = col 
            
            while i < len(mat) and j < len(mat[0]): 
                mat[i][j] = heapq.heappop(pq)
                i += 1 
                j += 1 
            
            j = col
            j += 1 
        
        return mat
        