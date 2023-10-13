class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def solve(i):
            if i>=n: return 0
            return cost[i]+min(solve(i+1),solve(i+2))
            
        return min(solve(0),solve(1))