class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n,m = len(strs),len(strs[0])
        p = {i : i for i in range(n)}
        
        def unite(i1,i2):
            p1,p2 = map(find,[i1,i2])
            p[p1]=p2
        def find(i):
            if p[i]==i: return i
            p[i]=find(p[i])
            return p[i]
        
        for idx,w1 in enumerate(strs):
            for idx2 in range(idx+1,n):
                w2 = strs[idx2]
                devCount = 0
                for j in range(m):
                    if w1[j]!=w2[j]: devCount+=1
                if devCount<=2:
                    unite(idx,idx2)
        
        return len(set([find(i) for i in range(n)]))
                