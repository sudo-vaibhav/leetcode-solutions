class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        tot = sum(piles)
        psum = [0]
        for p in piles:
            psum.append(psum[-1]+p)
        # print(psum)
        def cum_sum(i,j):
            return psum[j+1]-psum[i]
        
        @cache
        def solve(i,j):
            if i==j: return piles[i]
            s = cum_sum(i,j)
            # print(i,j,s)

            # if pick left one
            bob_collects = solve(i+1,j)
            ans = s-bob_collects
            
            # if pick right
            bob_collects = solve(i,j-1)
            ans = max(ans,s-bob_collects)
            return ans
        
        
        alice_collected = solve(0,n-1)
        return alice_collected>tot-alice_collected