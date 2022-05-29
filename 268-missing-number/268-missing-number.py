class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = (n*(n+1))//2
        S = sum(nums)
        diff = temp-S
        return diff