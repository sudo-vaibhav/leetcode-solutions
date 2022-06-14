class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l=0
        prod = 1
        ans=0
        for r in range(N):
            prod*=nums[r]
            while prod>=k and l<=r:
                prod//=nums[l]
                l+=1
            ans+=r-l+1
        
        return ans