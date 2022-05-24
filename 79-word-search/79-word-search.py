class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(i,j,idx,vis):
            if idx==len(word): return True
            for di,dj in moves:
                I,J = i+di,j+dj
                if 0<=I<m and 0<=J<n and (I,J) not in vis:
                    newAlpha = board[I][J]
                    if newAlpha==word[idx]:
                        vis.add((I,J))
                        if dfs(I,J,idx+1,vis):
                            return True
                        vis.remove((I,J))
            return False
                        
            
        for i in range(m):
            for j in range(n):
                cur = board[i][j]
                if cur==word[0]:
                    vis = set()
                    vis.add((i,j))
                    if dfs(i,j,1,vis):
                        return True
        return False
                    