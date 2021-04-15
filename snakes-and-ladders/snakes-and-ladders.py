from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        d = {1: 0} 
        q = deque()
        q.append(1)
        n = len(board)
        
        while q:
            curr = q.popleft()
            if curr == n*n:
                return d[curr]

            step = curr + 1
            
            for step in range(curr + 1, min(curr+6, n*n) +1):
                r, c = self.get(step, n)
                
                if board[r][c] != -1:
                    step = board[r][c]
                
                if step not in d:
                    d[step] = d[curr] + 1 
                    q.append(step)
                
        
        return -1 

    def get(self, num, n):
        div = (num-1) // n 
        mod = (num-1) % n 
        
        row = n - 1 - div 
        
        col = mod if row % 2 != (n % 2) else n - 1 - mod
        
        return (row, col)
                
        