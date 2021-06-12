from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q = deque()
        dist = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dist[start[0]][start[1]] = 0 
        q.append(start)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while q: 
            x1, y1 = q.popleft() 
            distance = dist[x1][y1]
            
            for pair in dirs:
                r = x1 + pair[0]
                c = y1 + pair[1]
                count = distance
                
                while 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1: 
                    r += pair[0]
                    c += pair[1]
                    count += 1 
                
                r -= pair[0]
                c -= pair[1]
                
                if count < dist[r][c]:
                    dist[r][c] = count 
                    q.append((r, c))
        
        res = dist[destination[0]][destination[1]]
    
        if res == float('inf'):
            return -1 
    
        return res
            
        