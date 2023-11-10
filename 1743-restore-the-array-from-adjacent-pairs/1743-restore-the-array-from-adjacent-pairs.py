class Solution:
    def restoreArray(self, ap: List[List[int]]) -> List[int]:
        temp = []
        for p in ap:
            temp.extend(p)
            
        ctr = Counter(temp)
        start = list(filter(lambda x:x[1]==1,ctr.items()))[0][0]
        seen = set()
        d = defaultdict(set)
        for u,v in ap:
            d[u].add(v)
            d[v].add(u)
        
        prev = start
        seen.add(start)
        ans = [start]
        
        while len(ans)!=len(ap)+1:
            nex = 0
            for v in d[prev]:
                if v not in seen:
                    ans.append(v)
                    seen.add(v)
                    prev = v
        return ans