class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        n = len(s)
        ans = (-inf,inf)
        baseCtr = Counter(t)
        ctr = defaultdict(int)
        
        def meetsCriteria():
            for k in baseCtr:
                if ctr[k]<baseCtr[k]:
                    return False
            return True
        
        while r<n:
            ctr[s[r]]+=1
            while meetsCriteria():
                prevLen = ans[1]-ans[0]+1
                newLen = r-l+1
                if newLen<prevLen:
                    ans = (l,r)
                ctr[s[l]]-=1
                l+=1
            r+=1
        
        if ans == (-inf,inf):
            return ""
        return s[ans[0]:ans[1]+1]