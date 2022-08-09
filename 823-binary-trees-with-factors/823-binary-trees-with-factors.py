class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr,MOD = set(arr),10**9+7
        @cache
        def solve(num):
            ans = 1
            for n in arr:
                if num%n==0 and num//n in arr:
                    ans = (ans+solve(n)*solve(num//n))%MOD
            return ans
        return sum([solve(n) for n in arr])%MOD