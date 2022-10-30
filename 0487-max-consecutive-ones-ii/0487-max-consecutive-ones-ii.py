class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l,r = 0,0
        oc = 0
        while r<n:
            oc += nums[r]==0
            while oc>1:
                oc -= nums[l]==0
                l+=1
            ans = max(ans,r-l+1)                
            r+=1
        return ans