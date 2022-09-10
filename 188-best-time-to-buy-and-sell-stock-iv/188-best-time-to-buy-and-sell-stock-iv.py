class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
#         N = len(prices)
#         if N<2:return 0
#         if k>=N/2:
#             return sum(max(a-b,0) for a,b in zip(prices[1:],prices[:-1]))
#         globalMax = defaultdict(int)
        
#         for transCount in range(1,k+1):
#             localMax = defaultdict(int)
#             for sellDay in range(1,N):
#                 profit = prices[sellDay]-prices[sellDay-1]
#                 localMax[sellDay] = max(
#                     globalMax[transCount-1,sellDay-1]+profit,
#                     globalMax[transCount-1,sellDay-1],
#                     localMax[sellDay-1]+profit
#                 )
#                 globalMax[transCount,sellDay] = max(globalMax[transCount,sellDay-1],
#                                                     localMax[sellDay])
        
#         return globalMax[k,N-1]

#         min_price = [inf] * (k + 1)
#         max_profit = [0] * (k + 1)
        
#         for price in prices:
#             for i in range(1, k + 1):
#                 min_price[i] = min(min_price[i], price - max_profit[i-1])
#                 max_profit[i] = max(max_profit[i], price - min_price[i])

#         return max_profit[k]
        N = len(prices)
        @cache
        def solve(i,k,currentlyBought):
            if i==N or k==0:return 0
            ans = solve(i+1,k,currentlyBought)
            if currentlyBought: ans = max(ans,solve(i+1,k-1,False)+prices[i])
            else: ans = max(ans,solve(i+1,k,True)-prices[i])
            return ans
        return solve(0,k,False)