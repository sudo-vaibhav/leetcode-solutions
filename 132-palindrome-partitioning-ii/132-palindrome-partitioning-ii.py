class Solution:
    def minCut(self, string: str) -> int:
        n = len(string)
        # dp = [[-1]*n for i in range(n)]
        @cache
        def isPalin(l,r):
            if l>=r:
                return True
            return string[l]==string[r] and isPalin(l+1,r-1)
        @cache
        def solve(l,r):
            # if dp[l][r]!=-1:return dp[l][r]
            if l>r or isPalin(l,r):
                # dp[l][r] = 0
                return 0
            else:
                ans = inf
                for midEnd in range(l,r):
                    if isPalin(l,midEnd):
                        ans = min(ans,solve(midEnd+1,r))
                # dp[l][r] = 1+ans
                return 1+ans
        return solve(0,len(string)-1)