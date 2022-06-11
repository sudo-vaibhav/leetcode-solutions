class Solution:
    def minimumCost(self, n: int, edges: List[List[int]]) -> int:
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(1,1+n)}
                self.distinct = n           
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu!=pv:
                    self.distinct-=1
                    self.parent[pu]=pv
            def find(self,u):
                if self.parent[u]!=u:
                    self.parent[u]=self.find(self.parent[u])
                return self.parent[u]
        
        uf = UF(n)
        edges.sort(key=lambda x:x[2])
        ans = 0
        for u,v,w in edges:
            if uf.find(u)==uf.find(v):
                pass
            else:
                uf.union(u,v)
                ans+=w
        return ans if uf.distinct==1 else -1 