class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sc,tc = set(source),set(target) # O(1) space
        for c in tc: # O(1)
            if c not in sc: return -1
        n = len(target)
        occs = defaultdict(list) # O(1)
        for idx,i in enumerate(source): # O(n)
            # if i not in occ:
            occs[i].append(idx)
        m = len(source)
        ti = 0
        si = 0
        ans = 1
        while ti<n: # O(n)
            curChar = target[ti]
            newSi = bisect_left(occs[curChar],si)
            # print(curChar,si,newSi)
            if newSi >= len(occs[curChar]):
                ans+=1
                si = 0
                continue
            si = occs[curChar][newSi]+1
            ti+=1
        return ans