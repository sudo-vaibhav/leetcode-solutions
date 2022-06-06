class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(n)}
                self.distinct = n
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                
                self.distinct-=1
                if pv<pu:
                    self.parent[pu]=pv
                else:
                    self.parent[pv]=pu
                    
                return True
            def find(self,v):
                if self.parent[v]!=v:
                    self.parent[v]=self.find(self.parent[v])
                return self.parent[v]
            def united(self):
                return self.distinct==1
            
        a = ord("a")
        uf = UF(26)
        
        for i in range(len(s1)):
            
            uf.union(ord(s1[i])-a,ord(s2[i])-a)
        
        ans = ""
        
        for s in baseStr:
            ans += chr(a+uf.find(ord(s)-a))
        
        return ans