class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        @cache
        def solve(idx,m):
            if idx>=N:
                return 0
            pickCounts = range(1,2*m+1)
            ans = -inf
            for pickCount in pickCounts:
                picked = sum(piles[idx:idx+pickCount])
                temp = max(pickCount,m)
                bobPickCounts = range(1,2*temp+1)
                bobStartIdx = idx+pickCount
                ans = max(ans,picked+sum(piles[bobStartIdx:])-solve(bobStartIdx,temp))
                # if bobStartIdx>=N:
                #     ans = max(ans,picked)
                # else:
                #     for bobPickCount in bobPickCounts:
                #         bobPicked = sum(piles[bobStartIdx:bobStartIdx+bobPickCount])
                #         mAfterBob = max(bobPickCount,temp)
                #         ans = max(ans,picked+solve(bobStartIdx+bobPickCount,mAfterBob))
            return ans
        
        return solve(0,1)