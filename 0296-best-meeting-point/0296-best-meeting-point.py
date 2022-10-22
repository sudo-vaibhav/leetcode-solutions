class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid),len(grid[0])
        rc,cc = [0]*m,[0]*n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rc[i]+=1
                    cc[j]+=1
        
        minDist = inf
        for i in range(m):
            for j in range(n):
#                 if this is the potential meeting spot
                dist = 0
                for row in range(m):
                    dist += rc[row]*abs(row-i)
                for col in range(n):
                    dist += cc[col]*abs(col-j)
                minDist = min(minDist,dist)
        
        return minDist