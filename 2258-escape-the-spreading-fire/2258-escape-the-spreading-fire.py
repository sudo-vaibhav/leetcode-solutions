def debug(something):
    return
    print(something)
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        ans = -inf
        rowCount,colCount = len(grid),len(grid[0])
        l,r = 0,1000000000
        grass,fire,wall = [0,1,2]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        def isPos(minutesWaited):
            GRID = deepcopy(grid)
            q = deque()
            for i in range(rowCount):
                for j in range(colCount):
                    cur = GRID[i][j]
                    if cur==fire:
                        q.append((i,j))

            # print("minutes waited",minutesWaited)
            # spread fire for m minutes
            for _ in range(0,minutesWaited,1):
                qsize = len(q)
                added = 0
                for i in range(qsize):
                    x,y = q.popleft()
                    for dx,dy in moves:
                        X,Y = x+dx,y+dy
                        if 0<=X<rowCount and 0<=Y<colCount and GRID[X][Y]==grass:
                            GRID[X][Y] = fire
                            added+=1
                            q.append((X,Y))
                if added == 0:
                    break
            # for row in GRID:
            #     print(row)
            travelQ = deque()

            vis = set()
            travelQ.append((0,0))
            debug("before walking")
            # for row in GRID:
            #     debug(row)
            # debug("iter done")
                
            while travelQ:
                
                            
                travelqsize = len(travelQ)
                # print(travelQ)
                moveadded = 0
                for i in range(travelqsize):
                    x,y = travelQ.popleft()
                    vis.add((x,y))
                    if x==rowCount-1 and y==colCount-1:
                        # print("here")
                        return True
                    if GRID[x][y]==fire:
                        continue
                    for dx,dy in moves:
                        X,Y = x+dx,y+dy
                        if 0<=X<rowCount and 0<=Y<colCount and GRID[X][Y]==grass and (X,Y) not in vis:
                            moveadded+=1
                            vis.add((X,Y))
                            travelQ.append((X,Y))
                qsize = len(q)
                for i in range(qsize):
                    x,y = q.popleft()
                    for dx,dy in moves:
                        X,Y = x+dx,y+dy
                        if 0<=X<rowCount and 0<=Y<colCount and GRID[X][Y]==grass:
                            GRID[X][Y] = fire
                            q.append((X,Y))
                # for row in GRID:
                #     debug(row)
                # debug("iter done")
                if moveadded==0:
                    break
            return False
            # account for spreading after leaving
            
            
        while l<=r:
            m = l+(r-l)//2
            debug(m)
            if isPos(m):
                ans = max(ans,m)
                l = m+1
            else:
                r = m-1
        debug("\n")
        if ans==-inf:
            return -1
        
        return ans