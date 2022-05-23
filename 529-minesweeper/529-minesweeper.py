class Solution:
    moves = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    
    def getAdjCount(self,board,i,j):
        adj = 0
        for di,dj in self.moves:
            I,J = i+di,j+dj
            if 0<=I<self.m and 0<=J<self.n and board[I][J]=="M":
                adj+=1
                
        return adj
                
            
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cr,cc = click
        self.m,self.n = len(board),len(board[0])
        
        cur = board[cr][cc]
        if cur=="M":
            board[cr][cc]="X"
        elif cur=="E":
            adj = self.getAdjCount(board,cr,cc)
            if adj>0:
                board[cr][cc] = str(adj)
            else:
                board[cr][cc] = "B"
                for di,dj in self.moves:
                    I,J = cr+di,cc+dj
                    if 0<=I<self.m and 0<=J<self.n:
                        self.updateBoard(board,[I,J])
        return board