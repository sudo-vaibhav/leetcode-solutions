class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        
        initState=(0,0,k)
        q = deque([initState])
        # q.append()
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        steps = 0
        seen = set([initState])
        if k>=m+n-2:
            return m+n-2
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                
                i,j,rLeft = q.popleft()
                if i==m-1 and j==n-1: return steps
                for di,dj in moves:
                    I,J = i+di,j+dj
                    if 0<=I<m and 0<=J<n:
                        newRLeft = rLeft - (grid[I][J]==1)
                        newState = (I,J,newRLeft)
                        if newRLeft>=0 and newState not in seen:
                            seen.add(newState)
                            q.append(newState)
            steps+=1
        
        return -1 
                    