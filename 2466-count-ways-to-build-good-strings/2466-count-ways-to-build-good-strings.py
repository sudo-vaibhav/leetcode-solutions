class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        MOD = 10**9+7
        
        @cache
        def solve(lenNeeded):
            if lenNeeded==0: return 1
            if lenNeeded<0: return 0
            ans = solve(lenNeeded-zero)+solve(lenNeeded-one)
            return ans%MOD
        
        ans = 0
        for lenNeeded in range(low,high+1):
            ans = (ans+solve(lenNeeded))%MOD
        return ans