class Solution:
    def minCut(self, string: str) -> int:
        n = len(string)
        @cache
        def isPalin(l,r):
            if l>=r:
                return True
            return string[l]==string[r] and isPalin(l+1,r-1)
        @cache
        def solve(i):
            if i==n:
                return -1
            if isPalin(i,n-1):
                return 0
            else:
                ans = inf
                for midEnd in range(i,n-1):
                    if isPalin(i,midEnd):
                        ans = min(ans,1+solve(midEnd+1))
                return ans
                    
        return solve(0)