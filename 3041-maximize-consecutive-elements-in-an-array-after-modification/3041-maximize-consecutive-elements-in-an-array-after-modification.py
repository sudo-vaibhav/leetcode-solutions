class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        global_max = 1
        for i in range(len(nums) - 1, -1, -1):
            dp[nums[i]] = 1 + dp[nums[i] + 1]
            dp[nums[i] + 1] = 1 + dp[nums[i] + 2]
            global_max = max(global_max, dp[nums[i]], dp[nums[i] + 1])

        return global_max