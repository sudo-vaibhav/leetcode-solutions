class Solution:
    def calcEquation(self, eqns, values, qrys):
        root = {}
        
        def find(x):
            parentX,ratioX = root.setdefault(x,(x,1.0))
            if parentX!=x:
                grandparent,grandparentratio = find(parentX)
                root[x] = (grandparent,grandparentratio*ratioX)
            return root[x]
        
        def union(u,v,val):
            parentU,ratioU,parentV,ratioV = *find(u),*find(v)
            if parentU!=parentV:
                root[parentU]= (parentV,val*(ratioV/ratioU))

        def getRatio(u,v):
            if u in root and v in root:
                parentU,ratioU,parentV,ratioV = *find(u),*find(v)
                if parentU!=parentV:
                    return -1.0
                else:
                    return ratioU/ratioV
            else:
                return -1.0
            
        for (u,v),val in zip(eqns,values): union(u,v,val)        
        return [getRatio(u,v) for u,v in qrys]
            
            