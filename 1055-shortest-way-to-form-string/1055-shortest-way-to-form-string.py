class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sc,tc = set(source),set(target) # O(1) space
        for c in tc: # O(1)
            if c not in sc: return -1
        m = len(source)
        n = len(target)
        occs = defaultdict(list) # O(1)
        nex = defaultdict(lambda : m)
        
        latestOcc = {}
        for idx in range(m-1,-1,-1):
            cur = source[idx]
            latestOcc[cur] = idx
            for alp in sc:
                if alp in latestOcc:
                    nex[idx,alp] = latestOcc[alp]
                    
        ti = 0
        si = 0
        ans = 1
        
#       with candidates starting from current index
        def getNextOcc(char,idx):
            return nex[idx,char]
        
        while ti<n: # O(n)
            curChar = target[ti]
            newSi = getNextOcc(curChar,si)
            if newSi >= m:
                ans+=1
                si = 0
                continue
            si = newSi+1
            ti+=1
        return ans