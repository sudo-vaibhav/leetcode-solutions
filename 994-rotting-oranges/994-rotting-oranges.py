class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        totalOrange = 0
        infected = 0
        empty,fresh,rotten = range(3)
        infected = deque()
        totInfected = 0
        totOranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==rotten:
                    infected.append((i,j))
                    totInfected+=1
                if grid[i][j]==rotten or grid[i][j]==fresh:
                    totOranges+=1
        time = 0
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        while infected and totInfected!=totOranges:
            N = len(infected)
            for _ in range(N):
                i,j = infected.popleft()
                for di,dj in moves:
                    I,J = i+di,j+dj
                    if 0<=I<m and 0<=J<n and grid[I][J]==fresh:
                        grid[I][J]=rotten
                        totInfected+=1
                        infected.append((I,J))
            time+=1
                
        
        if totOranges==totInfected:
            return time
        else:
            return -1
        
        
                