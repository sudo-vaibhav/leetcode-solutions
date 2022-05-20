class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        moves = [[1,0],[0,1]]
        
        @cache
        def solve(i,j):
            if grid[i][j]==1:
                return 0
            if j==n-1 and i==m-1:
                return 1
            else:
                ans = 0
                for di,dj in moves:
                    I,J = i+di,j+dj
                    if 0<=I<m and 0<=J<n and grid[I][J]!=1:
                        ans+=solve(I,J)
                return ans
                
        
        
        return solve(0,0)