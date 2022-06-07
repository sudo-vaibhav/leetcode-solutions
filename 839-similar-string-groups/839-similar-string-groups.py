class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = [list(s) for s in strs]
        
        class UF:
            def __init__(self,n):
                self.parent = [i for i in range(n)]
                self.size = [1 for i in range(n)]
                self.sz = n
            
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                else:
                    if self.size[pu]<self.size[pv]:
                        self.parent[pu]=pv
                    elif self.size[pu]>self.size[pv]:
                        self.parent[pv]=pu
                    else:
                        self.parent[pu]=pv
                        self.size[pv]+=1
                    self.sz-=1
                    return True
            
            def find(self,v):
                if self.parent[v]==v:
                    return v
                else:
                    self.parent[v] = self.find(self.parent[v])
                    return self.parent[v]
            
        N = len(strs)
        uf = UF(N)
        def comp(s1,s2):
            n = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    if n==2:
                        return False
                    n+=1
            return True
        
        for i in range(N):
            for j in range(i+1,N):
                if comp(strs[i],strs[j]):
                    uf.union(i,j)
        return uf.sz