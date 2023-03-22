class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        
        uf = {i:i for i in range(1,n+1)}
        
        def unite(u,v):
            pu,pv = map(find,[u,v])
            uf[pu]=pv
        
        def find(u):
            if uf[u]!=u:
                uf[u] = find(uf[u])
            # else:
            return uf[u]
        
        for u,v,c in roads:
            unite(u,v)
        
        C1 = find(1)
        ans = inf
        for u,v,c in roads:
            if find(u)==C1:
                ans = min(ans,c)
        return ans
        
        