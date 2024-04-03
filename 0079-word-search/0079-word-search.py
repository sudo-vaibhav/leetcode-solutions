class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = map(len,[board,board[0]])
        diffs = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def solve(idx,i,j,used):
            if idx==len(word)-1:
                return True
            for di,dj in diffs:
                I,J = i+di,j+dj
                if 0<=I<m and 0<=J<n and (I,J) not in used and word[idx+1]==board[I][J]:
                    used.add((I,J))
                    if solve(idx+1,I,J,used):return True
                    used.remove((I,J))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    used = set([(i,j)])
                    if solve(0,i,j,used):
                        return True
        
        return False
                    