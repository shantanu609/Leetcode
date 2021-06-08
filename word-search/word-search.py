class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 0):
                        return True 
    
        return False 
    
    def dfs(self, board, i, j, word, indx):
        # base case 
        if indx == len(word) -1:
            return True 
        
        # Logic 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ch = board[i][j]
        board[i][j] = -2 # visited 
        
        for pair in dirs: 
            r = i + pair[0]
            c = j + pair[1]
            
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == word[indx+1] :
                if self.dfs(board, r, c, word, indx + 1):
                    return True 
            
        board[i][j] = ch 
        return False