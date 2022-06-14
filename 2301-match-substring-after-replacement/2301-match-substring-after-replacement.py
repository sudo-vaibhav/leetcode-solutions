class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        m,n = len(s),len(sub)
        
        mapSet = defaultdict(set)
        for i in s:
            mapSet[i].add(i)
        for i in sub:
            mapSet[i].add(i)
        for u,v in mappings:
            mapSet[u].add(u)
            mapSet[u].add(v)
            
        def check(start):
            for i in range(n):
                if s[start+i] in mapSet[sub[i]]:
                    continue
                else:
                    return False
            return True
        
        for start in range(m):
            if start+n>m:
                 break
            if check(start):
                return True
        
        return False