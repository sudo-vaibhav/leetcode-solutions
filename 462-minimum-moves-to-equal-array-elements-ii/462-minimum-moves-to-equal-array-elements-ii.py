class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 1 4
#          5 => 2.5
#       1 4 -> 2 4 -> 3 4 -> 4 4
#       1 4 -> 2 4 -> 2 3 -> 3 3
        med = sorted(nums)[len(nums)//2]
        ans = sum([abs(med-num) for num in nums])
        return ans