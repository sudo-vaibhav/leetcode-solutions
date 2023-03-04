class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans,li,lmi,lma = 0,-1,-1,-1
        for i,cur in enumerate(nums):
            if cur<minK or cur>maxK:
                li=i
            if minK==cur:
                lmi=i
            if maxK==cur:
                lma=i
            if min(lmi,lma)>li:
                ans += min(lmi,lma)-li
        return ans
            
            
        