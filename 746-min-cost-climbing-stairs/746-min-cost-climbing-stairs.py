class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
        
#         @cache
#         def solve(i):
#             if i>=n:return 0
#             return cost[i] + min(
#                 solve(i+2),
#                 solve(i+1) #if i+1<n else inf
#             )
        
#         return min(solve(0),solve(1))

        n = len(cost)
        last = 0
        secondLast = 0
        for i in range(n-3,-1,-1):
            cur = min(secondLast+cost[i+1],last+cost[i+2])
            last = secondLast
            secondLast = cur
        return min(secondLast+cost[0],last+cost[1])
        