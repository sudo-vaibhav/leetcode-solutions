class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red,blue,green = range(3)
        colors = [red,blue,green]
        n = len(costs)
        @cache
        def solve(idx,prevColor):
            if idx==n:
                return 0
            else:
                ans = inf
                for color in colors:
                    if color!=prevColor:
                        ans = min(ans,costs[idx][color]+solve(idx+1,color))
                return ans
                
        
        
        return solve(0,4)