class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        for i in range(m):
            row = grid[i]
            for j in range(n):
                col = []
                for k in range(m):
                    col.append(grid[k][j])
                if row==col:
                    ans+=1
                    # ans.append((i,j))
        return ans