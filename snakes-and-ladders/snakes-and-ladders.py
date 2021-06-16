from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set() 
        n = len(board)
        q = deque([(1,0)])
        
        while q: 
            tag, moves = q.popleft()
            r, c = self.getRowCol(tag, n)
            if board[r][c] != -1: 
                tag = board[r][c]
            
            if tag == n*n:
                return moves 
            
            for nextSteps in range(1, 6+1): 
                newTag = tag + nextSteps
                
                if newTag <= n*n and newTag not in visited: 
                    visited.add(newTag)
                    q.append((newTag, moves + 1))
        
        return -1
    
    
    def getRowCol(self, tag, n):
        r, c = divmod(tag - 1, n)
        
        if r % 2 == 0: 
            return (n-1-r, c) 
        
        else: 
            return (n-1-r, n-1-c)
        