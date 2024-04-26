class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @cache
        def solve(i,j):
            if i==n-1:
                return grid[i][j]
            ans = inf
            for J in range(n):
                if J!=j:
                    ans = min(ans,grid[i][j]+solve(i+1,J))
            return ans
        
        return min([solve(0,j) for j in range(n)])