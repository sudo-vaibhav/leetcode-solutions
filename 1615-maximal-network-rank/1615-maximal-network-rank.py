class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        roads = set(map(tuple,roads))
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                ans = max(ans, len(adj[i])+len(adj[j])-(1 if (i,j) in roads or (j,i) in roads else 0 ))
                
        return ans