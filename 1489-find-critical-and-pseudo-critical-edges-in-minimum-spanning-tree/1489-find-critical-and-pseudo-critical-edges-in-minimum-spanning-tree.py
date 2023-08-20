class Solution:
    class UF:
        def __init__(self):
            self.p = {}
        def union(self,u,v):
            pu,pv = self.find(u),self.find(v)
            if pu!=pv:
                self.p[pu]=pv
                return True
            return False
        def find(self,u):
            pu = self.p.setdefault(u,u)
            if pu!=u:
                self.p[u] = self.find(self.p[u])
            return self.p[u]
        def is_joint(self,n):
            ref = self.find(0)
            for i in range(n):
                if self.find(i)!=ref:
                     return False
            return True
                
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        sorted_edges = list(sorted(enumerate(edges),key=lambda x:x[1][2]))
        uf = self.UF()
        mst_weight = 0
        for idx,(u,v,w) in sorted_edges:
            if uf.union(u,v):
                mst_weight += w
        crit,pseudo_crit = [],[]
        for idx, (u,v,w) in sorted_edges:
            uf = self.UF()
            # uf.union(u,v)
            wt = 0
            for idx2,(u2,v2,w2) in sorted_edges:
                if idx!=idx2 and uf.union(u2,v2):
                    wt+=w2
            is_crit = False
            if wt>mst_weight or not uf.is_joint(n):
                crit.append(idx)
                is_crit = True
            uf = self.UF()
            #compulsary union
            uf.union(u,v)
            wt = w
            for idx2,(u2,v2,w2) in sorted_edges:
                if idx2!=idx and uf.union(u2,v2):
                    wt+=w2
                    
            if wt == mst_weight and not is_crit:
                pseudo_crit.append(idx)
                
                
                        
                        
            
        
        return [crit,pseudo_crit]