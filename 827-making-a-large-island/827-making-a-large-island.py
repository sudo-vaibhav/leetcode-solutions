class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        islands = [[None for _ in range(n)] for _ in range(n)]
        land,water = 1,0
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        islandSize = defaultdict(int)

        for i in range(n):
            for j in range(n):
                cur = grid[i][j]
                if cur==land and islands[i][j]==None:
                    islandCode = (i,j)
                    islands[i][j]=islandCode
                    q = deque()
                    q.append((i,j))
                    size = 1
                    while len(q)>0:
                        curI,curJ = q.popleft()
                        for di,dj in moves:
                            I,J = curI+di,curJ+dj
                            if 0<=I<n and 0<=J<n and grid[I][J]==land and islands[I][J]==None:
                                islands[I][J]=islandCode
                                size+=1
                                q.append((I,J))
                    islandSize[islandCode]=size
        
#       standalone islands results case, take 1 as minimum since even water replaced once with land will yield island of area 1
        ans = 1 if len(islandSize)==0 else max(islandSize.values()) 
    
        
#         now lets see if combining can improve our result
        for i in range(n):
            for j in range(n):
                cur = grid[i][j]
                if cur==water:
#                     get distinct island codes in periphery
                    islandGroups = set()
                    for di,dj in moves:
                        I,J = i+di,j+dj
                        if 0<=I<n and 0<=J<n and islands[I][J]!=None:
                            islandGroups.add(islands[I][J])
#                         some growth can be achieved by joining islands
                    neighborIslandSizes = [islandSize[iGroup] for iGroup in islandGroups]
                    ans = max(ans,1+sum(neighborIslandSizes))
        
        return ans
                        
                