class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        
        @lru_cache(maxsize=10000)
        def solve(i,prevLate=0,prevAbs=0):
            if prevAbs==2:
                return 0
            if prevLate==3:
                return 0
            
            if i==n:
                return 1
            
            # if cur == "P":
            ans = solve(i+1,0,prevAbs)
            # if cur == "A":
            ans += solve(i+1,0,prevAbs+1)
            # if cur == "L":
            ans += solve(i+1,prevLate+1,prevAbs)
            return ans%MOD
            
        return solve(0,0,0)