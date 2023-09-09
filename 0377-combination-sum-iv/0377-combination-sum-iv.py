class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def solve(t):
            if t==0: return 1
            if t<0: return 0
            
            ans = 0
            for i in range(len(nums)):
                ans += solve(t-nums[i])
            return ans
        
        return solve(target)