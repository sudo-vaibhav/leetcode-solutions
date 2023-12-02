class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]<nums[j]>nums[k]:
                        ans = min(ans,nums[i]+nums[j]+nums[k])
        return ans if ans!=inf else -1