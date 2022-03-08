class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def solve(i,j):
            if(i==m-1 and j==n-1): return grid[i][j]
            if i==m or j==n : return float("inf")
            return grid[i][j]+min(solve(i+1,j),solve(i,j+1))
        
        return int(solve(0,0))