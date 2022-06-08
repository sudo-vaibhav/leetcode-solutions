class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        qrys = sorted(queries,key=lambda x:x[2])
        
        edges.sort(key=lambda x:x[2])
        
        E = len(edges)
        edgeIter = 0
        ans = {}
        
        class UF:
            
            parent = [i for i in range(n)]
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                self.parent[pu]=pv
            def find(self,u):
                if self.parent[u]==u:
                    return u
                self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
        
        uf = UF()
        for qry in qrys:
            p,q,thresh = qry
            
            while edgeIter<E and edges[edgeIter][2]<thresh:
                u,v,_ = edges[edgeIter]
                uf.union(u,v)
                edgeIter+=1
            
            ans[tuple(qry)]=(uf.find(p)==uf.find(q))
        
        return [ans[tuple(qry)] for qry in queries]