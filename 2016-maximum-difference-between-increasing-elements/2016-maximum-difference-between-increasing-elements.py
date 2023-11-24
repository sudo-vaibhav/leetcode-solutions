class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        minSoFar = nums[0]
        ans = -inf
        for i in range(1,len(nums)):
            ans = max(ans,nums[i]-minSoFar)
            minSoFar=  min(minSoFar,nums[i])
        return ans if ans>0 else -1