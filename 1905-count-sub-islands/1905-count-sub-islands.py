class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        
        def getMembership(grid):
            m,n = map(len,[grid,grid[0]])
            ansMap,ansIslands = {},defaultdict(list)
            
            visited = [[False for _ in range(n)] for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and grid[i][j]==1:
                        visited[i][j]=True
                        q = deque()
                        q.append((i,j))
                        while q:
                            u,v = q.popleft()
                            ansMap[(u,v)] = (i,j)
                            ansIslands[(i,j)].append((u,v))
                            for move in moves:
                                I = u+move[0]
                                J = v+move[1]
                                if I>=0 and I<m and J>=0 and J<n and not visited[I][J] and grid[I][J]==1:
                                    visited[I][J] = True
                                    q.append((I,J))
            return ansMap,ansIslands
                            
                        
            
        map1,islands1 = getMembership(grid1)
        _,islands2 = getMembership(grid2)
        ans = 0
        # print(map1,islands1,islands2)
        for islandBlock in islands2.keys():
            if islandBlock in map1:
                expected = map1[islandBlock]
                for block in islands2[islandBlock]:
                    if block not in map1 or map1[block] != expected:
                        break
                else:
                    ans+=1
        
        return ans
                