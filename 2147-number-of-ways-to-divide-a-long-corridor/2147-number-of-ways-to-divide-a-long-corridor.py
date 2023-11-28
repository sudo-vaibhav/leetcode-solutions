class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        d = [[None]*3 for _ in range(len(corridor))]
        # @lru_cache(maxsize=50000)
        def solve(i,seatsSoFar=0):
            
            # print(i,seatsSoFar,d)
            if d[i][seatsSoFar]!=None: return d[i][seatsSoFar]
            cur = corridor[i]
            if cur=="S":
                seatsSoFar+=1
            if seatsSoFar>2: return 0
            if i==len(corridor)-1:
                return int(seatsSoFar==2)
            ans = 0
            if seatsSoFar==2:
                ans += solve(i+1,0)
            ans += solve(i+1,seatsSoFar)
            
            if ans>=MOD:
                ans-=MOD
            d[i][seatsSoFar]=ans
            return d[i][seatsSoFar]
        
        return solve(0)