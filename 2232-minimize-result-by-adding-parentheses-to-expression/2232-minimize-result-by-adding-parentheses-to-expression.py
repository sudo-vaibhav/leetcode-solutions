class Solution:
    def minimizeResult(self, ex: str) -> str:
        a,b = ex.split("+")
        ans ="" 
        m=inf
        for l in range(len(a)): # keep before
            W = int(a[:l] or "1")
            X = int(a[l:])
            for r in range(len(b)): # keep after
                Y = int(b[:r+1])
                Z = int(b[r+1:] or "1")
                temp = W*(X+Y)*Z
                m = min(temp,m)
                if m==temp:
                    ans = a[:l]+"("+str(a[l:])+"+"+str(b[:r+1])+")"+str(b[r+1:])
        return ans