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
        endCost = [0]*n
        endCost[-1] = 0
        endCost[-2] = 0
        
        for i in range(n-3,-1,-1):
            endCost[i] = min(endCost[i+1]+cost[i+1],endCost[i+2]+cost[i+2])
        
        # print(endCost)
        return min(endCost[0]+cost[0],endCost[1]+cost[1])
        