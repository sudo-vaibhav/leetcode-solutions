class Solution:
    def equationsPossible(self,eqns: List[str]) -> bool:
        eqns.sort(key=lambda x:x[1],reverse=True)
        
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
        
        uf = UF(26)
        a = ord("a")
        for eqn in eqns:
            sym1,*op,sym2 = eqn
            if op[0]=="=":
                uf.union(ord(sym1)-a,ord(sym2)-a)
            else:
                t1,t2 = uf.find(ord(sym1)-a),uf.find(ord(sym2)-a)
                if t1==t2:
                    return False
        return True