class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2==1: return False
        t = tot//2
        @cache
        def solve(i,target):
            if i==len(nums):
                return target==0
            else:
                return solve(i+1,target) or solve(i+1,target-nums[i])
        return solve(0,t)
            