class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def getComponent(row,col):
            ans = set()
            ans.add((row,col))
            q = deque()
            q.append((row,col))
            origColor = grid[row][col]
            while q:
                i,j = q.popleft()
                
                for di,dj in moves:
                    I,J = i+di,j+dj
                    
                    if 0<=I<m and 0<=J<n and grid[I][J]==origColor and (I,J) not in ans:
                        ans.add((I,J))
                        q.append((I,J))
            return ans
            
            
            
        component = getComponent(row,col)
        
        
        for i,j in component:
            
            isBoundary = i==0 or j==0 or i==m-1 or j==n-1
            for di,dj in moves:
                I,J = i+di,j+dj
                if 0<=I<m and 0<=J<n and (I,J) not in component:
                    isBoundary = True
                    break
            
            if isBoundary:
                grid[i][j] = color
            
        return grid