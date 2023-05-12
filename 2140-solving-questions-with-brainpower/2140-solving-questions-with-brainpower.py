class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        n = len(qs)
        @cache
        def solve(i):
            if i>=n: return 0
            ans = solve(i+1)
            ans = max(ans,qs[i][0]+solve(i+qs[i][1]+1))
            return ans
    
        return solve(0)