class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    # if i==0:
                    #     ans+=1
                    # else:
                    if i==0 or grid[i-1][j]==0:
                        ans+=1
                    if i==m-1 or grid[i+1][j]==0:
                        ans+=1
                    if j==0 or grid[i][j-1]==0:
                        ans+=1
                    if j==n-1 or grid[i][j+1]==0:
                        ans+=1
        return ans
                        