class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = map(len,[grid,grid[0]])
        seen = set()
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j]==0:
                    q = deque([(i,j)])
                    valid = True
                    while q:
                        x,y = q.popleft()
                        for di, dj in moves:
                            I,J = x+di,y+dj
                            if 0<=I<m and 0<=J<n:
                                if grid[I][J]==0 and (I,J) not in seen:
                                    q.append((I,J))
                                    seen.add((I,J))
                            else:
                                valid = False
                    if valid:
                        ans +=1
        return ans
                    