class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        m,n = len(mat),len(mat[0])
        @cache
        def solve(i,j):
            if i>=m or j>=n:return 0
            cur = mat[i][j]
            
            if cur=="1":
                return 1+min(solve(i+1,j),solve(i,j+1),solve(i+1,j+1))
            else:
                return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,solve(i,j))
        return ans**2