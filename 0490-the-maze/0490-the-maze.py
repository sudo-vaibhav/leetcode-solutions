class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rowObs,colObs = defaultdict(list),defaultdict(list)
        for r in range(len(maze)):
            for c in range(len(maze[0])):
                if maze[r][c]==1:
                    rowObs[r].append(c)
                    colObs[c].append(r)
        seen = set()
        # returns if (i,j) is a coordinate from which destination can 
        # successfully be reached
        
        def canReach(i,j):
            
            if (i,j) in seen: return False
            # print(i,j)
            seen.add((i,j))
            if i==destination[0] and j==destination[1]: return True
            
            # up
            # bisect.bisect_left(colObs[j],i)
            for row in range(i-1,-1,-1):
                if maze[row][j]==1:
                    if canReach(row+1,j): return True
                    break
            else:
                if i!=0 and canReach(0,j): return True
            
            for row in range(i+1,len(maze)):
                if maze[row][j]==1:
                    if canReach(row-1,j): return True
                    break
            else:
                if i!=len(maze)-1 and canReach(len(maze)-1,j): return True
            
            for col in range(j+1,len(maze[0])):
                if maze[i][col]==1:
                    if canReach(i,col-1): return True
                    break
            else:
                if j!=len(maze[0])-1 and canReach(i,len(maze[0])-1): return True
            
            for col in range(j-1,-1,-1):
                if maze[i][col]==1:
                    if canReach(i,col+1): return True
                    break
            else:
                if j!=0 and canReach(i,0): return True
            return False
        
            
        
        
        return canReach(*start)