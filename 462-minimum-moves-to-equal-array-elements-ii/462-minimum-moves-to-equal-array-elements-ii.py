class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = sorted(nums)[len(nums)//2]
        ans = sum([abs(med-num) for num in nums])
        return ans