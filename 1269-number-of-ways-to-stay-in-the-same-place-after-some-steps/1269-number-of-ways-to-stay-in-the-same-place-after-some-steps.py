class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD =10**9+7
        # facMod = lambda x:1 if x==0 else (x*facMod(x-1))%MOD
        # for stayCount in range(0,steps+1):
        #     rest = steps - stayCount
        #     if rest%2==0:
        #         left = right = rest//2
        #         ans += factorial(steps)//(factorial(left)*factorial(right)*factorial(stayCount))
        # return ans
        @cache
        def solve(i,steps):
            if steps==0:
                return 0 if i!=0 else 1
            ans = solve(i,steps-1)
            if i-1>=0:
                ans = (ans+solve(i-1,steps-1))%MOD
            if i+1<arrLen:
                ans =  (ans+solve(i+1,steps-1))%MOD
            return ans
        return solve(0,steps)