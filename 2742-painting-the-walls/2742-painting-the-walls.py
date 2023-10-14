class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        walls = list(zip(cost,time))
        walls.sort(key=lambda x:(x[0],-x[1]))
        @lru_cache(maxsize=100000)
        def solve(i,timeRequiredByFreeSoFar):
            if i==n:
                if timeRequiredByFreeSoFar>0: return inf
                return 0
            # let free man paint this also
            ans = solve(i+1,timeRequiredByFreeSoFar+1)
            # or paint this yourself
            ans = min(ans,walls[i][0]+solve(i+1,max(-n,timeRequiredByFreeSoFar-walls[i][1])))
            return ans
        # for firstDoneByPaid in range(0,n-1):
            
        return solve(0,0)
            
        