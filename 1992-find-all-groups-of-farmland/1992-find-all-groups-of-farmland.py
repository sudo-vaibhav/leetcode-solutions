class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        seen = set()
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        ans = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    seen.add((i,j))
                    # ans += 1
                    q = deque([(i,j)])
                    mini,maxi = (i,j),(i,j)
                    while q:
                        (x,y) = q.popleft()
                        for di,dj in moves:
                            I,J = x+di,y+dj
                            if 0<=I<m and 0<=J<n and (I,J) not in seen and grid[I][J]==1:
                                seen.add((I,J))
                                if I<mini[0] or J<mini[1]:
                                    mini = (I,J)
                                if I>maxi[0] or J>maxi[1]:
                                    maxi = (I,J)
                                q.append((I,J))
                    ans.append([*mini,*maxi])
                                
        return ans