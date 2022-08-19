class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))
        n = len(nums)
        l,r = 0,n-1
        # if n==1: return 0
        # if nums[-1]>nums[-2]: return n-1
        while l<r:
            m = l+(r-l)//2
            if nums[m]>nums[m+1]:
                r = m
            else:
                l = m+1
        return l