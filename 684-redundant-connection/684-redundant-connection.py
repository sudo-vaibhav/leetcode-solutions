class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UF:
            def __init__(self):
                self.parent = dict()
                self.ranks = defaultdict(int)
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
                    puRank,pvRank = self.ranks[pu],self.ranks[pv]
                    sub,sup = pu,pv
                    if puRank>pvRank:
                        sub,sup = sup,sub
                    
                    if puRank==pvRank:
                        self.ranks[sup]+=1
                    self.parent[sub] = sup
                    return True
            
        uf = UF()

        for u,v in edges:
            if uf.union(u,v):
                continue
            else:
                return u,v
            