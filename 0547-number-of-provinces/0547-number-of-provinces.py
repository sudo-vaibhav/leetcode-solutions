class Solution:
    def findCircleNum(self, ic: List[List[int]]) -> int:
        n = len(ic)
        
        p = [i for i in range(n)]
        
        def unite(u,v):
            pu,pv = find(u),find(v)
            
            if pu!=pv:
                p[pu]=pv
        def find(u):
            if p[u]==u: return u
            p[u] = find(p[u])
            return p[u]
            
        for i in range(n):
            for j in range(n):
                if ic[i][j]==1:
                    unite(i,j)
        for i in range(n):
            find(i)
        return len(set(p))