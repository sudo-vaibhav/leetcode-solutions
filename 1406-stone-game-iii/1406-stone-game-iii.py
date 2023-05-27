class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        ps = []
        tot = sum(stoneValue)
        for i in range(0,n):
            if i-1>=0:
                tot-=stoneValue[i-1]
            ps.append(tot)
        ps.extend([0,0,0,0])
        # print(ps)
        
        tot = sum(stoneValue)
        @cache
        def solve(i):
            if i>=n: return 0
            ans = -inf
            for pick in range(1,4):
                # if i+pick<n:
                ans = max(
                ans,
                sum(stoneValue[i:i+pick])+
                ps[i+pick]-
                solve(i+pick)
                )
            return ans
        
        aliceStones = solve(0)
        
        if aliceStones>tot-aliceStones:
            return "Alice"
        elif aliceStones<tot-aliceStones:
            return "Bob"
        return "Tie"