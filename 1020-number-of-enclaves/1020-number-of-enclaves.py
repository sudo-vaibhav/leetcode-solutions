class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        done = [[False for j in range(n)] for i in range(m)]
        
        def isDesiredCell(i,j):
            return i==0 or j==0 or i==m-1 or j==n-1
        
        def isValidCell(i,j):
            return i>=0 and i<m and j>=0 and j<n
        ans = 0
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not done[i][j]:
                    done[i][j]=True
                    q = deque()
                    q.append((i,j))
                    
                    touched = False
                    c=0
                    while q:
                        curI,curJ = q.popleft()
                        c+=1
                        if isDesiredCell(curI,curJ):
                            touched = True
                        for move in moves:
                            I = curI+move[0]
                            J = curJ+move[1]
                            if isValidCell(I,J) and grid[I][J] == 1 and not done[I][J]:
                                done[I][J] = True
                                q.append((I,J))
                    if not touched:
                        ans += c
        return ans