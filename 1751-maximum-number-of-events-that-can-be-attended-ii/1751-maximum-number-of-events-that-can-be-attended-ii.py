class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = list(sorted(map(tuple,events)))
        # starts = list(map(lambda x:x[0],events))
        @cache
        def solve(i,picked):
            # if i>len(events):return -inf
            if i>=len(events):
                if picked<=k:
                    return 0
                return -inf
            else:
                ans = solve(i+1,picked)
                if picked<k:
                    start,end,rew = events[i]
                    new_idx = bisect_left(events,(end+1,))
                    ans = max(ans,rew+solve(new_idx,picked+1))
                return ans
        
        return solve(0,0)