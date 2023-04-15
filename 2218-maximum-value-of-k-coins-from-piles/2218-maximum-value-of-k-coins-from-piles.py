class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def solve(i,picks):
            if i==len(piles):
                # return -inf
                return 0
            else:
                # print(picks)
                ans = solve(i+1,picks)
                prev = 0
                for picked in range(0,min(len(piles[i]),picks)):
                    prev+=piles[i][picked]
                    ans = max(ans,prev+solve(i+1,picks-picked-1))
                return ans
            
        return solve(0,k)