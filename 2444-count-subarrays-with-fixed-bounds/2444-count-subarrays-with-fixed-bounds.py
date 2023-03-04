class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        n = len(nums)
        li,lmi,lma = -1,-1,-1
        ans = 0
        for i,cur in enumerate(nums):
            if cur<minK or cur>maxK:
                li=i
                
            if minK==cur:
                lmi=i
            if maxK==cur:
                lma=i
                
                
            if min(lmi,lma)>li:
                ans += min(lmi,lma)-li
                
#                 if cur==minK and lmi<=li:
#                     lmi = i
#                 if cur==maxK and lma<=li:
#                     lma = i
#             else:
#                 li = i
            
#             if li==i:
#                 for j in range(li+1,i+1):
#                     lmi =  
        
        return ans
            
            
        