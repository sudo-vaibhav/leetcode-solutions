class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        water,land = 0,1
        seen = [[False for _ in range(n)] for _ in range(m)]
        curIsland = set()
        islands = set()
        def dfs(i,j,initI,initJ):
            if 0<=i<m and 0<=j<n and grid[i][j]==land and not seen[i][j]:
                seen[i][j]=True
                curIsland.add((i-initI,j-initJ))
                moves = [0,1,0,-1,0]
                for di,dj in zip(moves[1:],moves[:-1]):
                    I,J = di+i,dj+j                    
                    dfs(I,J,initI,initJ)
                    
        for i in range(m):
            for j in range(n):
                curIsland = set()
                dfs(i,j,i,j)
                if len(curIsland)>0:
                    islands.add(tuple(curIsland))
                    
        return len(islands)