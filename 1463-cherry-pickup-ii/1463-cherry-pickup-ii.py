class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = map(len,[grid,grid[0]])
        # delts = [-1,0,1]
        @cache
        def solve(row,i,j):
            if row==m:
                return 0
            ans = 0
            # grid[row][i]+grid[row][j]
            for I in range(i-1,i+2):
                for J in range(j-1,j+2):
                    
                    if 0<=I<J<n:
                        ans = max(ans,grid[row][i]+grid[row][j]+solve(row+1,I,J))
            return ans
        
        return solve(0,0,n-1)