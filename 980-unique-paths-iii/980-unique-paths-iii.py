class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid),len(grid[0])
        
        start,end,blockCount = None,None,0
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if cur==1:
                    start = (i,j)
                elif cur==2:
                    end = (i,j)
                elif cur==-1:
                    blockCount+=1
        
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        # vis = set()
        def solve(i,j,path):
            nonlocal ans
            if (i,j)==end:
                if (len(path)==m*n-blockCount):
                    print(path)
                    ans+=1
            else:
                for di,dj in moves:
                    I,J = i+di,j+dj
                    if 0<=I<m and 0<=J<n and grid[I][J]!=-1 and (I,J) not in path:
                        path.append((I,J))
                        solve(I,J,path)
                        path.pop()
                    
        
        solve(start[0],start[1],[start])
        
        return ans