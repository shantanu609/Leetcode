import heapq
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
            B = box 
            T = Target 
            S = Player
            '.'  = free cell 
            '#' = obstacle
            
            Appraoch : A* algo 
                method : Heuristic = no. of moves + manhattan dist 
                moves 
        """
        pq = [] 
        visited = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        target = player = box = None 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'B':
                    box = (i, j)
                    continue 
                
                if grid[i][j] == 'S':
                    player = (i, j)
                    continue 
                
                if grid[i][j] == 'T':
                    target = (i, j)
                    continue 
        
        heapq.heappush(pq, (self.manhattanDist(box, target), 0, player, box))      #(Heur. , moves, player, box)
        
        while pq:
            dist, moves, player, box = heapq.heappop(pq)
            if (player, box) in visited:
                continue 
                
            visited.add((player, box))
            
            if box == target:  
                return moves 
            
            for pair in dirs: 
                r = player[0] + pair[0]
                c = player[1] + pair[1]
                
                if self.checkBound(grid, r, c) == False:
                    continue 

                    
                newPerson = (r, c)
                
                if newPerson == box: 
                    newBox = (pair[0] + box[0], pair[1] + box[1])
                    
                    if self.checkBound(grid, newBox[0], newBox[1]) == False:
                        continue
                    heapq.heappush(pq, (self.manhattanDist(newBox, target) + moves + 1, moves + 1, (r,c), newBox))
                
                else:
                    heapq.heappush(pq, (self.manhattanDist(box, target) + moves, moves, (r,c), box))
            
                
        return -1
                
    
    def manhattanDist(self, box, target):
        return abs(box[0] - target[0]) + abs(box[1] - target[1])
    
    def checkBound(self, grid, i , j):
        if i < 0 or j < 0 or i >= len(grid) or j  >= len(grid[0]):
            return False 
        
        if grid[i][j] == '#':
            return False 
    
        return True 