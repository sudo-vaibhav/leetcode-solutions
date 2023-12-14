class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rc,cc = defaultdict(int),defaultdict(int)
        m,n = map(len,[grid,grid[0]])
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val==1:
                    rc[i]+=1
                    cc[j]+=1
        diff = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                
                diff[i][j] = rc[i]+cc[j]-(m-rc[i])-(n-cc[j]) 
        return diff