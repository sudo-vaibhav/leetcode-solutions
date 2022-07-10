class TicTacToe:

    def __init__(self, n: int):
        self.rowCounts = defaultdict(int)
        self.colCounts = defaultdict(int)
        self.udCounts = defaultdict(int)
        self.ldCounts = defaultdict(int)
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        
        self.rowCounts[(row,player)]+=1
        self.colCounts[(col,player)]+=1
        
        if row==col:
            self.udCounts[player]+=1
        
        if row+col==self.n-1:
            self.ldCounts[player]+=1
        
        temp = [
            self.rowCounts[(row,player)],
            self.colCounts[(col,player)],
            self.udCounts[player],
            self.ldCounts[player]        
        ]
        
        # print(temp)
        for v in temp:
            if v==self.n:
                return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)