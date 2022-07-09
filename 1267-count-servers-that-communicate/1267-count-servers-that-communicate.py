class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        rc,cc = defaultdict(int),defaultdict(int)
        
        totalComps = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    totalComps+=1
                    rc[i]+=1
                    cc[j]+=1
        
        iso = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and rc[i]==1 and cc[j]==1:
                    iso+=1
        
        return totalComps - iso
        