class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        l,r = 0,0
        runSum = 0
        while r<N:
            runSum+=nums[r]
            while(runSum*(r-l+1)>=k):
                runSum-=nums[l]
                l+=1
            ans+=r-l+1
            r+=1
        return ans