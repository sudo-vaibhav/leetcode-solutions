class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dayMap = {0:1,1:7,2:30}
        
        @cache
        def solve(i,passTill=0):
            if i==len(days): return 0
            if passTill>=days[i]: return solve(i+1,passTill)
            
            ans = inf
            
            for idx,cost in enumerate(costs):
                ans = min(ans,cost+solve(i+1,days[i]+dayMap[idx]-1))
            
            return ans
        return solve(0)