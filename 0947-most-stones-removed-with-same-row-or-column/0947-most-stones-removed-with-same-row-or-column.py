class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        class UF:
            def __init__(self):
                self.p = {}
            def unite(self,u,v):
                pu,pv = self.find(u),self.find(v)
                self.p[pu]=pv
            def find(self,u):
                if u not in self.p:
                    self.p[u]=u
                if self.p[u]==u:
                    return u
                self.p[u] = self.find(self.p[u])
                return self.p[u]
        uf = UF()
        
        row = defaultdict(list)
        col = defaultdict(list)
        
        for i,j in stones:
            row[i].append((i,j))
            col[j].append((i,j))
        for sameRowCells in row.values():
            for cell in sameRowCells[1:]:
                uf.unite(sameRowCells[0],cell)
        for sameColCells in col.values():
            for cell in sameColCells[1:]:
                uf.unite(sameColCells[0],cell)
        parentToChildMapping = defaultdict(list)
        
        for cell in uf.p:
            parentToChildMapping[uf.find(cell)].append(cell)
        ans = 0
        for k in parentToChildMapping:
            ans += len(parentToChildMapping[k])-1
        return ans
                