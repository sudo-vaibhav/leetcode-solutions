class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def solve(i):
            if i>=n:return 0
            
            return min(
                cost[i]+solve(i+2),
                (cost[i]+solve(i+1)) #if i+1<n else inf
            )
        
        return min(solve(0),solve(1))