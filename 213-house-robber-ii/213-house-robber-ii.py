class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        
        def solve(nums,i,dp={}):
            if i in dp:
                return dp[i]
            if i<0:
                dp[i] = 0
                return  0
            else:
                dp[i] = max(nums[i]+solve(nums,i-2,dp),solve(nums,i-1,dp))
                return dp[i]
        
        n = len(nums)
        dp1,dp2 = {},{}
        return max(solve(nums[1:],n-2,{}),solve(nums[:-1],n-2,{}))