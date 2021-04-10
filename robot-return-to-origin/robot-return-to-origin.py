class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #         R        L       U        D 
        dirs = [[1, 0], [-1, 0], [0, 1],[0, -1]]
        move = {"R":0, "L":1, "U":2, "D":3}
        x = 0
        y = 0 
        for ch in moves:
            index = move[ch]
            pair = dirs[index]
            
            x += pair[0]
            y += pair[1]
        
        if x == 0 and y == 0:
            return True 
        
        return False
            