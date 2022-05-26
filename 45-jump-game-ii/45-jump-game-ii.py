class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def solve(idx):
            if idx>=N-1: return 0
            # if idx==N-1:
            #     return 0
            val = nums[idx]
            ans = inf
            for jumps in range(1,val+1):
                ans = min(ans,1+solve(idx+jumps))
            return ans
        return solve(0)