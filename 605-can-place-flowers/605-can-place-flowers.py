class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        
        @cache
        def solve(idx):
            if idx>=N:
                return 0
            else:
                dontPlant = solve(idx+1) if flowerbed[idx]==0 else solve(idx+2)
                ans = dontPlant
                if flowerbed[idx]==0 and (idx==0 or flowerbed[idx-1]==0) and (idx==N-1 or flowerbed[idx+1]==0):
#                     can plant here
                    ans = max(ans,1+solve(idx+2))
                return ans
        return solve(0)>=n
        