class Solution:
    def minSteps(self, n: int) -> int:
        # seen = set()
        @cache
        def solve(onScreen=1,onClip=0):
            
            # seen.add((onScreen,onClip))
            
            # print(onScreen,onClip)
            if onScreen==n:
                return 0
            if onScreen>n:
                return inf
#           if i copy on clip, i will incur a step
            ans = inf
            if onScreen>onClip:
                ans = 1+solve(onScreen,onScreen)
#           or i can paste current clip
            if onClip>0:
                ans = min(ans,1+solve(onScreen+onClip,onClip))
            return ans
        return solve()
            
        