class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        running = 0
        for num in nums:
            running += num
            ans |= running|num
        return ans