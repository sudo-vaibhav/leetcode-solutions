class Solution:
    def getTup(self,board):
        return tuple([tuple(row) for row in board])
    def getZero(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    return i,j
        
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        fin = [[1,2,3],[4,5,0]]
        moves = [-1,0,1,0,-1]
        seen = set()
        seen.add(self.getTup(board))
        steps = 0
        if board==fin:
            return 0
        q = deque()
        q.append(board)
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                cur = q.popleft()
                if cur==fin:
                    return steps
                i,j = self.getZero(cur)
                
                for x in range(4):
                    di,dj = moves[x],moves[x+1]
                    I,J = i+di,j+dj
                    if 0<=I<2 and 0<=J<3:
                        cur[i][j],cur[I][J] = cur[I][J],cur[i][j]
                        tupBoard = self.getTup(cur)
                        if tupBoard not in seen:
                            seen.add(tupBoard)
                            q.append(deepcopy(cur))
                        cur[i][j],cur[I][J] = cur[I][J],cur[i][j]
                        
                
            steps+=1
            
        return -1
        