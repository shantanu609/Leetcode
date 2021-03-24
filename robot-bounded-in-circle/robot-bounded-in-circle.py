class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        #       N      E.     S      W
        x, y = 0, 0 
        direction = 0   # North 
        
        for ch in instructions:
            if ch == 'L':
                direction = (direction + 3) % 4 
            
            elif ch == 'R':
                direction = (direction + 1) % 4 
            
            elif ch == 'G':
                x += dirs[direction][0]
                y += dirs[direction][1]
            
        if (x == 0 and y == 0) or direction != 0:
            return True 
        
        return False 