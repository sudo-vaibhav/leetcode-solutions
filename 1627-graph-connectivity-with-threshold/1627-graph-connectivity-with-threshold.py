class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(1,n+1)}
            def union(self,u,v):
                # print("uni",u,v)
                pu,pv = self.find(u),self.find(v)
                self.parent[pu]=pv
            def find(self,v):
                if self.parent[v]==v:
                    return v
                else:
                    self.parent[v] = self.find(self.parent[v])
                    return self.parent[v]
        uf = UF(n)
        for t in range(threshold+1,n+1):
            mult=2
            
            while mult*t<=n:
                temp = mult*t
                uf.union(temp,t)
                mult+=1
        
        ans = []
        for u,v in queries:
            ans.append(uf.find(u)==uf.find(v))
                
        return ans