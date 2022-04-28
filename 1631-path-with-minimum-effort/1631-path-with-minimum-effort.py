class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = []
        n,m = len(heights),len(heights[0])
        heappush(q,(0,0,0))
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = [[inf for j in range (m)] for i in range(n)]
        seen[0][0]=0
        ans = inf
        while q:
            
            eff,i,j = heappop(q)
            if eff>seen[i][j]:continue
            if i==n-1 and j==m-1:
                return eff
            else:
                for di,dj in moves:
                    I,J=i+di,j+dj
                    if 0<=I<n and 0<=J<m:
                        newEff = max(eff, abs(heights[i][j]-heights[I][J]))
                        temp = (newEff,I,J)
                        if seen[I][J]>newEff:
                            seen[I][J]=newEff
                            heappush(q,temp)
                        
                    
        return ans
            