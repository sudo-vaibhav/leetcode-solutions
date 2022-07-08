class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
#       start buying from day, se max profit kya hoga
        @cache
        def solve(day):
            if day >= n:
                return 0
            ans = 0
            minPriceBefore = prices[day]
            for nextSellDay in range(day+1,n):
                ans = max(ans,max(0,prices[nextSellDay]-minPriceBefore)+solve(nextSellDay+2))
                minPriceBefore = min(minPriceBefore,prices[nextSellDay])
            return ans
                
        return solve(0)