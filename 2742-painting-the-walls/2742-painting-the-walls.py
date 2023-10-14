class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @lru_cache(maxsize=None)
        def solve(i,timeRequiredByFreeSoFar):
            if i==n:
                if timeRequiredByFreeSoFar>0: return inf
                return 0
            ans = min(
                # let free man paint this also
                solve(i+1,timeRequiredByFreeSoFar+1),
                # or paint this yourself, max check to prevent 
                # dp swelling up (anyways dont need more than n time from prev steps)
                cost[i]+solve(i+1,max(-n,timeRequiredByFreeSoFar-time[i])))
            return ans
            
        return solve(0,0)
            
        