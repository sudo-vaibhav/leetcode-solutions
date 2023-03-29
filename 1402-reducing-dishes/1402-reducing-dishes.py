class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        n = len(sat)
        sat.sort()
        @cache
        def solve(i,place):
            if i==n: return 0
            
            ans = solve(i+1,place)
            
            ans = max(ans,sat[i]*place+solve(i+1,place+1))
            return ans
        
        return solve(0,1)