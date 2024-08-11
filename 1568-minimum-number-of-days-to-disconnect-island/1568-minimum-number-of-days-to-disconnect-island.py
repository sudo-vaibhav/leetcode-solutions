class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        vals = []
        m,n = map(len,(grid, grid[0]))
        for row in grid:
            vals.extend(row)
        c = Counter(vals)
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        def findIslands():
            seen = set()
            islands = {}
            c=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and (i,j) not in seen:
                        c+=1
                        seen.add((i,j))
                        q = deque([(i,j)])
                        islands[(i,j)] = (i,j)
                        while q:
                            x,y = q.popleft()
                            for di,dj in moves:
                                I,J = x+di,y+dj
                                if 0<=I<m and 0<=J<n and grid[I][J]==1 and (I,J) not in seen:
                                    prev = islands[(i,j)]
                                    islands[(i,j)] = (max(prev[0],I),max(prev[1],J))
                                    # if I>i or J>j:
                                    #     islands[(i,j)]=(I,J)
                                    # if I==i or J==j:
                                    #     islands[(i,j)]=(max(I,i))
                                    q.append((I,J))
                                    seen.add((I,J))
            return islands
        ic = findIslands()
        if len(ic)!=1:
            return 0                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if len(findIslands())!=1: return 1
                    grid[i][j]=1
                
        return 2