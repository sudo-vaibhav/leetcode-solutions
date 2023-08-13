class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def solve(i):
            if i==n:
                return True
            ans = False
            if i<=n-2 and nums[i]==nums[i+1]:
                ans |= solve(i+2)
            if i<=n-3 and nums[i]==nums[i+1]==nums[i+2]:
                ans |= solve(i+3)
            if i<=n-3 and nums[i]==nums[i+1]-1==nums[i+2]-2:
                ans |= solve(i+3)
            return ans
                
        
        
        return solve(0)