class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(i,prev=False):
            if i==len(nums):
                return 0
            ans = solve(i+1,False)
            if prev==False:
                ans = max(ans,nums[i]+solve(i+1,True))
            return ans
        return solve(0)