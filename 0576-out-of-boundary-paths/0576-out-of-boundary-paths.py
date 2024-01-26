class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 10**9+7
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        def isOutOfBounds(i,j):
            return i==-1 or i==m or j==-1 or j==n
            
        @cache
        def solve(i,j,movesLeft):
            if isOutOfBounds(i,j):
                return 1
                # return 0
            elif movesLeft==0:
                return 0
            else:
                ans = 0
                for (di,dj) in moves:
                    I,J = i+di,j+dj
                    ans += solve(I,J,movesLeft-1)%MOD
                return ans%MOD
                    
        
        return solve(startRow,startColumn,maxMove)