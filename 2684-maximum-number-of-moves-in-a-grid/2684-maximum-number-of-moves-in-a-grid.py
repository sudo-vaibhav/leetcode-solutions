class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if j==len(grid[0])-1:
                return 0
            ans = 0
            for m in [-1,0,1]:
                I = i+m
                if 0<=I<len(grid) and grid[I][j+1]>grid[i][j]:
                    ans = max(ans,1+solve(I,j+1))
            return ans
        
        return max([solve(i,0) for i in range(len(grid))])