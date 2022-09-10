class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        if N<2:return 0
        if k>=N/2:
            return sum(max(a-b,0) for a,b in zip(prices[1:],prices[:-1]))
        globalMax = defaultdict(int)
        
        for transCount in range(1,k+1):
            localMax = defaultdict(int)
            for sellDay in range(1,N):
                profit = prices[sellDay]-prices[sellDay-1]
                localMax[sellDay] = max(
                    globalMax[transCount-1,sellDay-1]+profit,
                    globalMax[transCount-1,sellDay-1],
                    localMax[sellDay-1]+profit
                )
                
                globalMax[transCount,sellDay] = max(globalMax[transCount,sellDay-1],localMax[sellDay])
        
        return globalMax[k,N-1]