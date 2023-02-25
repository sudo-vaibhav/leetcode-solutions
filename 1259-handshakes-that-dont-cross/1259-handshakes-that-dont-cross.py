class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9+7
        
        @cache
        def solve(n):
            if n<=2: return 1
            ans = 0
            for hsWith in range(2,n+1,2):
                onClockSide = hsWith-2
                onAntiClockSide = n-onClockSide-2
                ans = (ans+solve(onClockSide)*solve(onAntiClockSide))%MOD
                
            return ans
        
        return solve(numPeople)
            