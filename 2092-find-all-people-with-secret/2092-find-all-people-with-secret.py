class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        timewise = defaultdict(list)
        
        
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
            timewise[time].append(peeps)
        
        for i in sorted(timewise.keys()):
            scoped_uf = UF()
            for u,v in timewise[i]:
                scoped_uf.unite(u,v)
            toadd = set()
            for u,v in timewise[i]:
                if overall.find(u)==0 or overall.find(v)==0:
                    toadd.add(scoped_uf.find(u))
                    toadd.add(scoped_uf.find(v))
            for u,v in timewise[i]:
                if scoped_uf.find(u) in toadd:
                    overall.unite(u,0)
                if scoped_uf.find(v) in toadd:
                    overall.unite(v,0)
             
        ans = []
        for i in range(n):
            if overall.find(0)==overall.find(i):
                ans.append(i)
        return ans
            # find(0)