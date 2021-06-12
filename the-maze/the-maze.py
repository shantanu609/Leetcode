from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque()
        q.append(start)
        maze[start[0]][start[1]] = 2        # MARK AS VISITED
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q: 
            x1, y1 = q.popleft()    
            
            if x1 == destination[0] and y1 == destination[1]:
                return True 
            
            for pair in dirs:
                r = x1 + pair[0]
                c = y1 + pair[1]
                
                while 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1: 
                    r = r + pair[0]
                    c = c + pair[1]
                
                r = r - pair[0]
                c = c - pair[1]
                
                if maze[r][c] == 0: 
                    q.append((r, c))
                    maze[r][c] = 2    
        
        return False