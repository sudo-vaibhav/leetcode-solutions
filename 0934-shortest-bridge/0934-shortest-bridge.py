class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        i1,j1 = None,None
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    i1,j1 = i,j
                    break
            if i1!=None: break
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        island1 = [(i1,j1)]
        seen = set(island1)
        q = deque([(i1,j1)])
        while q:
            cur = q.popleft()
            for di,dj in moves:
                I,J = cur[0]+di,cur[1]+dj
                if 0<=I<n and 0<=J<n and (I,J) not in seen and grid[I][J]==1:
                    island1.append((I,J))
                    seen.add((I,J))
                    q.append((I,J))
        
        # print(island1)
        
        q = deque(island1)
        
        dist = 1
        
        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                i,j = q.popleft()
                
                for di,dj in moves:    
                    I,J = i+di,j+dj
                    if 0<=I<n and 0<=J<n and (I,J) not in seen:
                        if grid[I][J]==1: return dist-1
                        else:
                            seen.add((I,J))
                            q.append((I,J))
                    
            dist+=1
        return 0
        
        