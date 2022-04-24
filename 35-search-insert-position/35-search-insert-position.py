class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target>nums[n-1]:
            return n
        if target<nums[0]:
            return 0
        l,r = 0,n-1
        ans = inf
        while l<=r:
            m = l+(r-l)//2
            if nums[m]<target:
                
                l = m+1
            elif nums[m]==target:
                return m
            else:
                ans = min(ans,m)
                r = m-1
        return ans
        