class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        @cache
        def solve(rolls,target):
            if rolls==0:
                if target==0:
                    return 1
                return 0
            
            ans = 0
            for curRoll in range(1,k+1):
                ans = (ans+solve(rolls-1,target-curRoll))%MOD
            return ans
        
        
        return solve(n,target)