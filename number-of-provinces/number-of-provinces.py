class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        count = 0 
        
        for row in range(len(isConnected)):
            if visited[row] == 0:
                self.dfs(isConnected, row, visited)
                count += 1 
        
        return count 
    
    def dfs(self, isConnected, row, visited):
        # base case 
        
        
        # logic 
        for col in range(len(isConnected[0])):
            if isConnected[row][col] == 1 and visited[col] == 0:
                visited[col] = 1 
                self.dfs(isConnected, col, visited)
                