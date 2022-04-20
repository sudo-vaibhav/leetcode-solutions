class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t = sorted(nums)
        l,r = inf,-inf
        for idx in range(len(nums)):
            if t[idx]!=nums[idx]:
                l = min(idx,l)
                r = max(idx,r)
        print(l,r)
        return max(r-l+1,0)