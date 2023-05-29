class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.r = defaultdict(lambda:defaultdict(int))
        self.c = defaultdict(lambda:defaultdict(int))
        self.ld = {1:0,2:0}
        self.ud = {1:0,2:0}
        
    def move(self, row: int, col: int, player: int) -> int:
        self.r[row][player]+=1
        self.c[col][player]+=1
        
        if row==col:
            self.ld[player]+=1
        if row+col==self.n-1:
            self.ud[player]+=1
        
        for pyr in [1,2]:
            for num in range(0,self.n):
                if self.r[num][pyr]==self.n: return pyr
                if self.c[num][pyr]==self.n: return pyr
            if self.ld[pyr]==self.n or self.ud[pyr]==self.n : return pyr 

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)