class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def solve(amt,i):
            if amt==0: return 1
            if i==len(coins):return 0
            cc = 0
            ans = 0
            while amt-cc*coins[i]>=0:
                ans += solve(amt-cc*coins[i],i+1)
                cc+=1
            return ans
        return solve(amount,0)
            