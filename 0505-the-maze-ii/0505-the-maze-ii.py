class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n= len(maze),len(maze[0])
        MAZE = [[1]*(n+2)]
        for row in maze:
            newRow = [1,*list(row),1]
            # newRow.extend()
            # newRow.append(1)
            MAZE.append(newRow)
        MAZE.append([1]*(n+2))        
        dest = (destination[0]+1,destination[1]+1)
        START = (start[0]+1,start[1]+1)
        
        @cache
        def findBallDest(i,j,di,dj):
            try:
                while MAZE[i][j]==0:
                    i+=di
                    j+=dj
                return i-di,j-dj
            except:
                print(i,j,di,dj)
        
        dists = defaultdict(lambda:inf)
        dists[START]=0
        
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        hp = [(0,START)]
        while hp:
            d,point = heappop(hp)
            i,j = point
            if d>dists[point]:continue
            for di,dj in moves:
                I,J = findBallDest(i,j,di,dj)
                newDist = abs(i-I)+abs(j-J)+d
                if dists[(I,J)]>newDist:
                    dists[(I,J)]=newDist
                    heappush(hp,(newDist,(I,J)))
                    
        
        
            
            
        ans=dists[dest]
        return ans if ans!=inf else -1
        
# def solve(i,j):
#     # if MAZE[i][j]!=0: return inf
#     if i==dest[0] and j==dest[1]: return 0
#     ans = inf
#     for di,dj in moves:
#         I,J = findBallDest(i,j,di,dj)
#         if (I,J) not in seen:
#             seen.add((I,J))
#             ans = min(ans,abs(i-I)+abs(j-J)+solve(I,J))
#             seen.remove((I,J))
#     return ans
        
        
        