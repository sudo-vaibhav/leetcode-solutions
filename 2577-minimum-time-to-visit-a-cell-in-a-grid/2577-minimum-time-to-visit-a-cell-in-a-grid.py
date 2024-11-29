class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1],grid[1][0])>1:
            return -1
        m,n = map(len,[grid,grid[0]])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        hp = [(0,0,0)]
        dists = defaultdict(lambda:defaultdict(lambda:inf))
        dists[0][0]=0
        while hp:
            # print(hp[0])
            timeOfVisit,i,j = heappop(hp)
            
            for di,dj in moves:
                I,J = i+di,j+dj
                if 0<=I<m and 0<=J<n:
                    newDist = 1+timeOfVisit if grid[I][J]<=timeOfVisit+1 else None
                    if not newDist:
                        temp = grid[I][J]#-timeOfVisit
                        if temp%2==timeOfVisit%2:
                            temp+=1
                        newDist = temp
                        # 2->2,3-4,4->4
                        # 3->3,4->5
                    if newDist<dists[I][J]:
                        dists[I][J] = newDist
                        heappush(hp,(newDist,I,J))
        return dists[m-1][n-1] if dists[m-1][n-1]!=inf else -1
        
        