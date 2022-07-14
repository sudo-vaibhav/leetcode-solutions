class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==1:
                    for di,dj in moves:
                        I,J = i+di,j+dj
                        if 0<=I<m and 0<=J<n and grid[I][J]==1:
                            pass
                        else:
                            ans += 1
        return ans
                            