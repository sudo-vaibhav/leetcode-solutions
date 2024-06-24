class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        fliptill = []
        ans = 0
        for i in range(n):
            cur = nums[i]
            flips = len(fliptill)-bisect_left(fliptill,i)
            # donefor = bisect_right(fliptill,i-k+1)
            end = flips
            postAdjust = cur if (end)%2==0 else 1-cur
            flipNeeded = postAdjust==0
            # print(i,cur,flips,postAdjust,flipNeeded,end,fliptill)
            if flipNeeded:
                final = i+k-1
                if final>=n:
                    return -1
                fliptill.append(final)
                ans += 1
        return ans