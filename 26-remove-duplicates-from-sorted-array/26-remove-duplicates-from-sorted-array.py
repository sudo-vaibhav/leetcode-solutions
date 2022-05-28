class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        k=0
        while r<n:
            while r<n and nums[r]==nums[l]:
                r+=1
            nums[k] = nums[l]
            k+=1
            l = r
        return k