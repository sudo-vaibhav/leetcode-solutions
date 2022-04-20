class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t = sorted(nums)
        l,r = inf,-inf
        for idx in range(len(nums)):
            if t[idx]!=nums[idx]:
                if idx<l:
                    l = idx
                if idx>r:
                    r = idx
        if r-l+1>0:
            return r-l+1
        return 0