class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        
        for i in nums:
            max_or |= i
        
        
        @cache
        def solve(i,cur):
            if i==len(nums):
                return int(cur==max_or)
            ans = solve(i+1,cur)
            ans += solve(i+1,cur|nums[i])
            return ans
        return solve(0,0)