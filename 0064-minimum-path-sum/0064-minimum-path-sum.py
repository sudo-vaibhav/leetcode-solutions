class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = map(len,[grid,grid[0]])
        @cache
        def solve(i,j):
            if i==m or j==n: return inf
            if i==m-1 and j==n-1: return grid[i][j]
            return grid[i][j]+min(solve(i+1,j),solve(i,j+1))
        
        return solve(0,0)