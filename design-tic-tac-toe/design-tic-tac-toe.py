class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n 
        self.row = [0] * n 
        self.col = [0] * n 
        self.d = 0 
        self.sd = 0 

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        play = -1 if player == 1 else 1 
        
        self.row[row] += play 
        self.col[col] += play 
        
        if row == col:
            self.d += play
        
        if row + col == self.n - 1:
            self.sd += play 
        
        if self.n in self.row or self.n in self.col or self.n == self.d or self.n == self.sd:
            return 2 
        
        if -self.n in self.row or -self.n in self.col or -self.n == self.d or -self.n == self.sd:
            return 1
        
        return 0 
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)