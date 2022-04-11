class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        p_vis = [[False for _ in range(n)] for _ in range(m)]
        a_vis = [[False for _ in range(n)] for _ in range(m)]
        
        p_reach,a_reach = set(),set()
        
        def dfs(i,j,vis,reach):
            vis[i][j]=True
            reach.add((i,j))
            for di,dj in moves:
                I,J = i+di,j+dj
                if I<0 or I>=m or J<0 or J>=n or vis[I][J] or heights[I][J]<heights[i][j]:
                    continue
                dfs(I,J,vis,reach)
            
        for i in range(m):
            dfs(i,0,p_vis,p_reach)
            dfs(i,n-1,a_vis,a_reach)
        
        for j in range(n):
            dfs(0,j,p_vis,p_reach)
            dfs(m-1,j,a_vis,a_reach)
        print(p_reach,a_reach)
        return p_reach.intersection(a_reach)