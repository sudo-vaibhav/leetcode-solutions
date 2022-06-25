class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thresh: int) -> int:
        adj = [[inf if i!=j else 0 for j in range(n)] for i in range(n)]
        
        for u,v,wt in edges:
            adj[u][v]=wt
            adj[v][u]=wt
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])
                    adj[j][i] = min(adj[j][i],adj[j][k]+adj[k][i])
        minCit = inf
        minCount = inf
        # print(*adj,sep="\n")
        for i in range(n):
            ct=0
            for dist in adj[i]:
                if dist<=thresh:
                    ct+=1
            # print(i,ct)
            if ct<=minCount:
                minCit = i
                minCount = ct
        # print("-")
        return minCit