class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UF:
            def __init__(self):
                self.parent = dict()
            def find(self,v):
                if v not in self.parent:
                    return v
                else:
                    p = self.parent[v]
                    self.parent[v] = self.find(p)
                    return self.parent[v]
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                else:
                    mi = min(pu,pv)
                    other = pu if pu!=mi else pv
                    self.parent[other] = mi
                    return True
            
        uf = UF()

        for u,v in edges:
            if uf.union(u,v):
                continue
            else:
                return u,v
            