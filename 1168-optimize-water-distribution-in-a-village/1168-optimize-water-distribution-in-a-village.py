class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        ops = pipes
        for idx, well in enumerate(wells):
            ops.append((0,idx+1,well))
        
        
        ops.sort(key=lambda x:x[2])
        
        hyd = set()
        ans = 0
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(0,1+n)}
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
        
        for op in ops:
            # print(op)
            u,v,c = op
            if uf.find(u)==uf.find(v):
                pass
            else:
                # if u==v:
                ans+=c
                hyd.add(u)
                hyd.add(v)
                uf.union(u,v)
            
        
        return ans
            