# Time = O(m x n x max(m x n)), max because we are going deeper from each wall cell
# Space = O(m x n )

from collections import deque
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # q = deque()
        dist = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dist[start[0]][start[1]] = 0 
        # q.append(start)
        pq = [] 
        stopped = set()
        heapq.heappush(pq, (0, start[0], start[1]))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while pq: 
            distance, x1, y1 = heapq.heappop(pq)
            stopped.add((x1, y1))
            # distance = dist[x1][y1]
            if dist[x1][y1] < distance: 
                continue 
            
            for pair in dirs:
                r = x1 + pair[0]
                c = y1 + pair[1]
                count = distance
                
                # BALL ROLLING UNTIL WE HIT THE WALL 
                while 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1: 
                    r += pair[0]
                    c += pair[1]
                    count += 1 
                
                # COME BACK ONE STEP AS WE JUST ENTERED THE WALL CELL IN THE MAZE
                r -= pair[0]
                c -= pair[1]
                
                # UPDATE THE DISTANCE IS ITS LESSER THAN PREVIOUSLY KNOWN
                if count < dist[r][c]:
                    dist[r][c] = count 
                    # q.append((r, c))
                    if (r,c) not in stopped:
                        heapq.heappush(pq, (count, r, c))
        
        res = dist[destination[0]][destination[1]]
    
        if res == float('inf'):
            return -1 
    
        return res
            
        