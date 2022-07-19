class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        oneOff,allEql = 0,1
        @cache
        def solve(i,j):
            if i<0 or j<0:
                return (0,0)
            prev = solve(i-1,j-1)
            res = [None,None]
            if s[i]==t[j]:
                res[oneOff] = prev[oneOff]
                res[allEql] = prev[allEql]+1
            else:
                res[oneOff] = prev[allEql]+1
                res[allEql] = 0
            return res
                
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += solve(i,j)[0]
        return ans                         
