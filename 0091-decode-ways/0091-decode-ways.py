class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {}
        n = len(s)
        for i in range(26):
            mapping[str(i+1)]=chr(ord("A")+i)
        @cache
        def solve(i):
            if i==n:
                return 1
            ans = 0
            if s[i] in mapping :
                ans += solve(i+1)
            if i!=n-1 and s[i:i+2] in mapping:
                ans += solve(i+2)
            return ans
        return solve(0)
                