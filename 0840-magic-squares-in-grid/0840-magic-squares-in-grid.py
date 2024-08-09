class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m,n = map(len,[grid,grid[0]])
        ans = 0
        def checkMat(u,v):
            seen = set()
            # if u+2<m and v+2<n:
            nums = set()
            for row in range(u,u+3):
                temp = 0
                for col in range(v,v+3):
                    temp += grid[row][col]
                    nums.add(grid[row][col])
                seen.add(temp)
            for col in range(v,v+3):
                temp = 0
                for row in range(u,u+3):
                    temp += grid[row][col]
                seen.add(temp)
            
            temp = 0
            for k in range(3):
                temp += grid[u+k][v+k]
            seen.add(temp)
            seen.add(grid[u][v+2]+grid[u+1][v+1]+grid[u+2][v])
            # print(seen,u,v)
            return len(seen)==1 and nums==set(range(1,10))
            # else:
            #     return False
        for i in range(m-2):
            for j in range(n-2):
                if checkMat(i,j):
                    ans += 1
        return ans