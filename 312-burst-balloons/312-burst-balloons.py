class Solution:
    
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = (1,*nums,1)
        
        @cache
        def solve(l , r):
            if(l>=r): return 0
            else:
                ans = -1
                for k in range(l,r):
                    tempans = (nums[l-1] * nums[k] * nums[r]) + solve(l,k) + solve(k+1,r)
                    ans = max(ans,tempans)
                return ans
        return solve(1,n+1)