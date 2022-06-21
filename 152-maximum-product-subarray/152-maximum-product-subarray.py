class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans,max_streak,min_streak = nums[0],nums[0],nums[0]
        
        for i in range(1,n):
            cur = nums[i]
            new_max_streak = max(cur,cur*max_streak,cur*min_streak)
            min_streak = min(cur,cur*max_streak,cur*min_streak)
            max_streak = new_max_streak
            ans = max(ans,max_streak)
        return ans
            