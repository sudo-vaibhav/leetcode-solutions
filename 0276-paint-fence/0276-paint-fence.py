class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache
        def solve(i,reduced):
            if i==n:
                return 1
            if i>n:
                return 0
            ans = 0
            for j in range(k-int(reduced)):
                ans += solve(i+2,True)+solve(i+1,True)
            return ans
            
        
        return solve(0,False)