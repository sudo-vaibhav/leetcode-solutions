class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        candBefore,candAfter = None,None
        for u,v in edges:
            if v in parent:
                candBefore = parent[v],v
                candAfter = u,v
                continue
            parent[v] = u        
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(1,n+1)}
                
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                else:
                    self.parent[pu] = self.parent[pv]
                    return True
                
            def find(self,v):
                if self.parent[v]==v: return v
                self.parent[v] = self.find(self.parent[v])
                return self.parent[v]
    
        uf = UF(len(edges))
        if candBefore==None:
#             no node with 2 parents, only cycle is there
            for u,v in edges:
                if uf.union(u,v):
                    continue
                else:
                    return u,v
        else:
            
#             now cycle maybe present or not present
#             lets ignore one candidate and and see if cycle still persists
            cycFound = False
            for u,v in edges:
                if (u,v) == candAfter:
                    continue # one skipped
                if uf.union(u,v):
                    continue
                else:
                    return candBefore
            
            return candAfter