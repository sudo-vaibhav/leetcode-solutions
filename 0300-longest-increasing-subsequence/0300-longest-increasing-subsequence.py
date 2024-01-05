class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def solve(i):
            if i==n:
                return 0
            ans = 1
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    ans = max(ans,1+solve(j))
            return ans
        ans=0
        for i in range(n):
            ans = max(ans,solve(i))
        return ans