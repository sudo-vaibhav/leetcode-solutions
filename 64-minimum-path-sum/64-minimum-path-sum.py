# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         @cache
#         def solve(i,j):
#             if(i==m-1 and j==n-1): return grid[i][j]
#             if i==m or j==n : return float("inf")
#             return grid[i][j]+min(solve(i+1,j),solve(i,j+1))
#         return int(solve(0,0))

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf") for j in range(n+1)] for i in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if m-1==i and n-1==j: continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        # for l in dp:
        #     print(*l)
        return dp[0][0]