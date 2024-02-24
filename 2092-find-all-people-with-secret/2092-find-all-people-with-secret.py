class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know = set([0,firstPerson])
        ctr = defaultdict(list)
        
        
        class UF:
            def __init__(self):
                self.p = {}
            def unite(self,u,v):
                pu,pv = map(self.find,[u,v])
                if pu!=pv:
                    self.p[max(pu,pv)]=min(pu,pv)

            def find(self,u):
                if u not in self.p:
                    self.p[u]=u
                if self.p[u]==u:
                    pass
                else:
                    self.p[u]=self.find(self.p[u])
                return self.p[u]
        
        
        overall = UF() 
        overall.unite(0,firstPerson)
        
        meetings.sort(key=lambda x:x[-1])
        
        for *peeps,time in meetings:
            ctr[time].append(peeps)
        
        for i in sorted(ctr.keys()):
            scoped_uf = UF()
            for u,v in ctr[i]:
                scoped_uf.unite(u,v)
            toadd = set()
            for u,v in ctr[i]:
                if overall.find(u)==0 or overall.find(v)==0:
                    toadd.add(scoped_uf.find(u))
                    toadd.add(scoped_uf.find(v))
            for u,v in ctr[i]:
                if scoped_uf.find(u) in toadd:
                    overall.unite(u,0)
                if scoped_uf.find(v) in toadd:
                    overall.unite(v,0)
                
            
            
#             for peeps in ctr[i]:
                
#                 if any(map(lambda x:find(x)==find(0),peeps)):
#                     unite(*peeps)
#             for peeps in ctr[i][::-1]:
                
#                 if any(map(lambda x:find(x)==find(0),peeps)):
#                     unite(*peeps)
                        
        ans = []
        for i in range(n):
            if overall.find(0)==overall.find(i):
                ans.append(i)
        return ans
            # find(0)