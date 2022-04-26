class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,n = 0,len(nums)
        r = n-1
        if n==1: return nums[0]
        def getTwiceUpperBound(idx):
            if idx<n-1 and nums[idx+1]==nums[idx]:
                return idx+1
            if idx>0 and nums[idx-1]==nums[idx]:
                return idx
            return -1
        while l<=r:
            m = l+(r-l)//2
            temp = getTwiceUpperBound(m)
            if temp == -1:
                return nums[m]
            if temp%2==1:
                l = m+1
            else:
                r = m-1
        return -1
        