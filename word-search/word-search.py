class Solution:
    dirs = None 
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True 
                    if self.dfs(board, i, j, visited, word, 1):
                        return True 
                    visited[i][j] = False 
        
        return False 
    
    def dfs(self, board, i, j, visited, word, indx):
        # base case 
        if indx == len(word):
            return True 
        
        # logic 
        # mark the i,j as visited 
        
        # explore neighoring skills 
        for pair in self.dirs:
            visited[i][j] = True
            r = pair[0] + i 
            c = pair[1] + j 
            
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and visited[r][c] == False and board[r][c] == word[indx]: 
                if self.dfs(board, r, c, visited, word, indx + 1):
                    return True 
            visited[i][j] = False
        return False 
        