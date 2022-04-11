class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def s(n,amt):
            if amt==0: return 1
            if n==0: return 0
            cur = coins[n-1]
            ans = 0
            for cOfCurrentType in range(0,1+(amt//cur)):
                ans+=s(n-1,amt-cOfCurrentType*cur)
            return ans
        return s(n,amount)