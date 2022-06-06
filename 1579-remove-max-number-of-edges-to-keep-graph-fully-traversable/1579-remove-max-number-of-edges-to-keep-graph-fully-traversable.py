class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        class UF:
            def __init__(self,n):
                self.parent = {i:i for i in range(1,n+1)}    
                self.distinct = n
            def union(self,u,v):
                pu,pv = self.find(u),self.find(v)
                if pu==pv:
                    return False
                self.parent[pu] = self.parent[pv]
                self.distinct-=1
                return True
            
            def connected(self):
                return self.distinct == 1
            
            def find(self,v):
                if self.parent[v]!=v:
                    self.parent[v] = self.find(self.parent[v])
                return self.parent[v]
        
        aliceUF,bobUF = UF(n),UF(n)
        both,alice,bob = 3,1,2
        used = 0
        
        edges.sort(reverse=True,key=lambda x:x[0])
        
        for edgeType,u,v in edges:
            if edgeType==both:
                if aliceUF.union(u,v) | bobUF.union(u,v):
                    used+=1
            elif edgeType==alice:
                if aliceUF.union(u,v):
                    used+=1
            else:
                if bobUF.union(u,v):
                    used+=1
                
        if aliceUF.connected() and bobUF.connected():
            return len(edges)-used   
        else:
            # print(aliceUF.distinct,bobUF.distinct)
            return -1
            