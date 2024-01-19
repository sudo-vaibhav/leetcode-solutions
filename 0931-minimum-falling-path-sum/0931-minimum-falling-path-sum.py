class Solution:
    # @cache
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i==len(matrix):
                return 0
            if j<0 or j>=len(matrix[0]):
                return inf
            else:
                return matrix[i][j]+min(solve(i+1,j-1),solve(i+1,j),solve(i+1,j+1))
        ans = inf
        for j in range(len(matrix)):
            ans = min(ans,solve(0,j))
        return ans