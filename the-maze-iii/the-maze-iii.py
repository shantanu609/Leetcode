import heapq
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        pq = []
        heapq.heappush(pq, (0, "", ball[0], ball[1]))
        stopped = {(ball[0], ball[1]) : [0, ""]}
        dirs = [[-1, 0, 'u'], [1,0,'d'], [0,-1,'l'], [0,1,'r']]
        
        while pq: 
            dist, string, i, j = heapq.heappop(pq)
            
            if [i, j] == hole:
                return string 
        
            for x, y, s in dirs: 
                r = i
                c = j
                count = dist
                
                while 0 <= r + x < len(maze) and 0 <= c + y < len(maze[0]) and maze[r+x][c+y] != 1: 
                    r += x 
                    c += y 
                    count += 1 
                    
                    if [r,c] == hole:
                        break 
     
                if (r,c) not in stopped or [count, string + s] < stopped[(r, c)]: 
                    stopped[(r,c)] = [count, string + s]
                    heapq.heappush(pq, (count, string + s, r, c))
        
        return "impossible"