class Solution:
    def calcEquation(self, eqns, values, qrys):
        root = {}
        
        def find(x):
            xp,xr = root.setdefault(x,(x,1.0))
            if xp!=x:
                grandparent,grandparentratio = find(xp)
                root[x] = (grandparent,grandparentratio*xr)
            return root[x]
        
        def union(u,v,val):
            pu,ru,pv,rv = *find(u),*find(v)
            if pu!=ru:
                root[pu]= (pv,val*rv/ru)

        @cache
        def getRatio(u,v):
            if u in root and v in root:
                pu,ru,pv,rv = *find(u),*find(v)
                if pu!=pv:
                    return -1.0
                else:
                    return ru/rv
            else:
                return -1.0
        for (u,v),val in zip(eqns,values): union(u,v,val)        
        return [getRatio(u,v) for u,v in qrys]
            
            