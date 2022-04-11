class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k==0: return grid
        m,n = len(grid),len(grid[0])
        prev = grid[m-1][n-1]
        for i in range(m):
            for j in range(n):
                grid[i][j],prev = prev,grid[i][j]
        return self.shiftGrid(grid,k-1)