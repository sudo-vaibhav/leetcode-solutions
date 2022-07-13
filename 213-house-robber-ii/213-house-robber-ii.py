class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        
        def solve(nums):
            secondLast,last = 0,0
            cur = 0
            for i in range(len(nums)):
                cur = max(nums[i]+secondLast,last)
                secondLast = last
                last = cur
            
            return cur
            # if i<0:
            #     dp[i] = 0
            #     return  0
            # else:
            #     dp[i] = max(nums[i]+solve(nums,i-2,dp),solve(nums,i-1,dp))
            #     return dp[i]
        
        return max(solve(nums[1:]),solve(nums[:-1]))