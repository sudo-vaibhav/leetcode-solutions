class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            
        # print(adj)
        self.possible = True
        col = {i:-1 for i in range(1,n+1)}
        
        def dfs(i,color):
            col[i]=color
            for dest in adj[i]:
                if col[dest]==-1:
                    dfs(dest,1-color)

                elif col[dest]==color:
                    self.possible = False
                    return 
            
        for i in range(1,n+1):
            if col[i]==-1:
                dfs(i,0)
        # print(col)       
        return self.possible
        
        