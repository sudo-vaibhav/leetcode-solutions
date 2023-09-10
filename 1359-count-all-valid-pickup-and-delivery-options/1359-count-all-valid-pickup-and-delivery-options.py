class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def solve(pi,di):
            if di==0 and pi==0:return 1
            if di<0 or pi<0 or di<pi: return 0
            ans = pi*solve(pi-1,di)
            ans += (di-pi)*solve(pi,di-1)
            ans %= MOD
            return ans
            
        return solve(n,n)