class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        *rest,sl,l=sorted(nums)
        if l>=2*sl:
            return nums.index(l)
        return -1