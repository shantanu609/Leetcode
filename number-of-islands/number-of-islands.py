class DSU:
    def __init__(self, size):
        self.array = [i for i in range(size)]
        self.size = size 
        
    def find(self, num):
        if self.array[num] != num:
            self.array[num] = self.find(self.array[num])
        
        return self.array[num]

    def union(self, num1, num2) -> bool:
        parent1 = self.find(num1)
        parent2 = self.find(num2)
        
        if parent1 == parent2: 
            # there is no union to be done 
            return False
         
        self.array[parent1] = parent2
        return True 
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dsu = DSU(m*n)
        
        res = 0 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1 
                    
                    for pair in dirs: 
                        r = i + pair[0]
                        c = j + pair[1]
                        
                        if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                            cell_1 = (i * n) + j 
                            cell_2 = (r * n) + c 
                            
                            if dsu.union(cell_1, cell_2): 
                                # they both are a part of one island. So reduce result count 
                                res -= 1 
        
        return res