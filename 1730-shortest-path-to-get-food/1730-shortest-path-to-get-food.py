class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        start,food,free,block = "*#OX"
        # print(block)
        START = None
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if cur==start:
                    START = i,j
                    break
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        
        vis = set()
        q = deque()
        vis.add((START[0],START[1]))
        q.append(START)
        
        steps = 0
        while q:
            lenQ = len(q)
            
            for _ in range(lenQ):
                i,j = q.popleft()
                if grid[i][j]==food:
                    return steps
                for di,dj in moves:
                    I,J = i+di,j+dj
                    if 0<=I<m and 0<=J<n and (I,J) not in vis and grid[I][J]!=block:
                        vis.add((I,J))
                        q.append((I,J))
                    
            steps+=1
        return -1