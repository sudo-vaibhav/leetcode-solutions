class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        MOD = 10**9+7
        @cache
        def solve(num):
            ans = 1
            
            for n in arr:
                if num%n==0:
                    rest = num//n
                    if rest in arr:
                        ans += solve(n)*solve(rest)
                        if ans >= MOD:
                            ans-=MOD
            return ans
        
        return sum([solve(n) for n in arr])%MOD