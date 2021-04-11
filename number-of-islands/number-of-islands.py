class DSU:
    def __init__(self, m):
        self.parent = [i for i in range(m)]
        self.count = m
        
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        
        return self.parent[num]
        
    
    def union(self, num1, num2):
        p1 = self.find(num1)
        p2 = self.find(num2)
        if p1 == p2:
            return False 
        
        self.parent[p1] = p2
        return True 

    def getCount(self):
        
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                self.count -= 1 
        
        return self.count
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
            
        dsu = DSU(m * n)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        count = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1 
                
                    for pair in dirs:
                        r = i + pair[0]
                        c = j + pair[1]
                        
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                            if dsu.union((i * n) + j, (r * n) + c):
                                count -= 1 
                    
        return count
        
        
        