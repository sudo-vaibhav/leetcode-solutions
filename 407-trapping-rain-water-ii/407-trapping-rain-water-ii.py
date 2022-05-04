class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        m,n,ans = len(h),len(h[0]),0
        vis = [[False for _ in range(n)] for _ in range(m)]
        
        minQ = []
        
        for row in range(m):
            vis[row][0] = True
            vis[row][n-1] = True
            heappush(minQ,(h[row][0],row,0))
            heappush(minQ,(h[row][n-1],row,n-1))
            
        for col in range(n):
            vis[0][col] = True
            vis[m-1][col] = True
            heappush(minQ,(h[0][col],0,col))
            heappush(minQ,(h[m-1][col],m-1,col))
        
        diffs = [[-1,0],[1,0],[0,1],[0,-1]]
        while minQ:
            curHeight,i,j = heappop(minQ)
            for di,dj in diffs:
                I,J = i+di,j+dj
                if 0<=I<m and 0<=J<n and not vis[I][J]:
                    vis[I][J] = True
                    ans += max(0,curHeight-h[I][J])
                    h[I][J] = max(curHeight,h[I][J])
                    heappush(minQ,(h[I][J],I,J))
        return ans
            
            