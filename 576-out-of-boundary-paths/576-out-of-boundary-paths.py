class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove==0:
            return 0
        dp = [[[0 for _ in range(0,maxMove+1)] for _ in range(n)] for _ in range(m)]
        for col in range(n):
            if col==0 or col==n-1:
#                 full mark case
                for i in range(m):
                    dp[i][col][1] = 1
            else:
#                 non full mark case
                dp[0][col][1] = 1
                dp[m-1][col][1] = 1
        dp[0][0][1] = 2
        dp[m-1][n-1][1] = 2
        dp[0][n-1][1]=2
        dp[m-1][0][1]=2
        MOD = 10**9+7
        if m==1 or n==1:
            if m==1 and n==1:
                dp[0][0][1] = 4
            else:
                for i in range(m):
                    for j in range(n):
                        dp[i][j][1]+=1
        
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        for movesCount in range(2,maxMove+1):
            for i in range(m):
                for j in range(n):
                    for di,dj in moves:
                        I,J = i+di,j+dj
                        if 0<=I<m and 0<=J<n:
                            dp[i][j][movesCount] += dp[I][J][movesCount-1]
                            if dp[i][j][movesCount]>=MOD:
                                dp[i][j][movesCount]-=MOD 
        ans= 0
        for i in range(1,maxMove+1):
            ans += dp[startRow][startColumn][i]
            if ans>=MOD:
                ans -= MOD
        return ans
            