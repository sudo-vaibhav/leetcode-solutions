class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(n)}
                self.distinct = n
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                self.distinct-=1
                self.parent[pu]=pv
                return True
            def find(self,v):
                if self.parent[v]!=v:
                    self.parent[v]=self.find(self.parent[v])
                return self.parent[v]
            def united(self):
                return self.distinct==1
        uf = UF(n)
        for time,u,v in logs:
            uf.union(u,v)
            if uf.united():
                return time
        
        return -1