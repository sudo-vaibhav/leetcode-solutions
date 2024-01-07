class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = defaultdict(lambda:defaultdict(int))
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                res+= dp[j][diff]
                dp[i][diff] += 1+dp[j][diff]
        return res