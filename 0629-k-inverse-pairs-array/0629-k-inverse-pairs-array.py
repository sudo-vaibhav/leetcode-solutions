class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        # if k==0:
        #     return 1
#         returns number of possibilities to make array of n elements with k inversions
        @cache
        def solve(n,k):
            if n==0:
                return 0
            if k==0:
                return 1
            # print(n,k)
#            upto n-1 shifts we can do on n-1 step result arrays
            ans = (solve(n-1,k) - (solve(n-1,k-n) if k-n>=0 else 0))%MOD
            return (ans+solve(n,k-1))%MOD
        return (solve(n,k)- (solve(n,k-1) if k>0 else 0))%MOD