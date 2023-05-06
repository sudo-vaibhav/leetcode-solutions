class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n,MOD = len(nums),10**9+7
        nums.sort()
        l,r = 0,n-1
        ans = 0
        while l<=r:
            if nums[l]+nums[r]<=target:
                ans = (ans+pow(2,r-l,MOD))%MOD 
                l+=1
            else:
                r-=1
        return ans