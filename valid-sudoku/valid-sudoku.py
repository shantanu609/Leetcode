class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows 
        for row in board:
            res = self.checkRowHelper(row)
            if res == False:
                print('1')
                return False 
        
        # check columns 
        res = self.checkColHelper(board)
        if res == False:
            print('2')
            return False 
        
        # check 3 x 3 sub-boxes 
        res = self.checkBoxes(board)
        if res == False :
            print('3')
            return False 
    
        return True 
    
    def checkRowHelper(self, row):
        d = set()
        for num in row:
            if num == ".":
                continue 
            if num in d:
                return False 
            d.add(num)
        
        return True 
    
    def checkColHelper(self, board):
        for j in range(len(board[0])):
            d = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue 
                num = board[i][j]
                if num in d:
                    return False 
                d.add(num)
    
        return True 
    
    def checkBoxes(self, board):
        r1, r2, c1, c2 = 0, 2, 0, 2
        
        while r1 < len(board):
            if c1 >= len(board[0]):
                c1 = 0 
                c2 = 2 
            
            d = set()
            j = r1 
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    num = board[i][j]
                    if num == '.':
                        continue 
                    if num in d:
                        return False 
                    d.add(num)
            print(d)
            c1 += 3 
            c2 += 3 
            if c1 >= len(board[0]):
                r1 += 3 
                r2 += 3 
        
        return True
            
                