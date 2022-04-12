class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for c in connections:
            adj[c[0]].append(c[1])
            adj[c[1]].append(c[0])
        visited = [False for i in range(n)]
        # print(adj)
        def dfs(comp,parent):
            ew = 0
            for neig in adj[comp]:
                if not visited[neig]:
                    visited[neig]=True
                    ew+=dfs(neig,comp)
                else:
                    if neig != parent:
                        ew+=1
            return ew
                    
        connectedComponents = 0
        ew=0
        for comp in range(n):
            if not visited[comp]:
                visited[comp] = True
                ew+=dfs(comp,-1)//2
                connectedComponents+=1
        # print(ew)
        if ew < connectedComponents-1:
            return -1
        else: return connectedComponents-1
        
        