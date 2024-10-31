class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factories = []
        for f,c in factory:
            factories.extend([f]*c)
        factories.sort()
        @lru_cache(maxsize=10000)
        def solve(ri,fi):
            if ri==len(robot):
                return 0
            if fi==len(factories):
                return inf
            ans = solve(ri,fi+1)
            ans = min(ans,abs(robot[ri]-factories[fi])+solve(ri+1,fi+1))
            return ans
        return solve(0,0)