class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBefore = inf
        maxProfit = 0
        for i in range(len(prices)):
            cur = prices[i]
            maxProfit = max(maxProfit,cur-minBefore)
            minBefore = min(minBefore,cur)
        return maxProfit