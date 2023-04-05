class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
#         l,r = 1,max(nums)
#         ans = r
#         while l<=r:
#             m = (l+r)//2
#             prev = 0
#             for i in range(len(nums)-1,0,-1):
#                 cur = nums[i]+prev
#                 if cur<=m:
#                     prev=0
#                 else:
#                     prev = cur-m
#             if prev+nums[0]>m:
#                 l = m+1
#             else:
#                 ans = m
#                 r = m-1
#         return ans
            
    
        pf=ans=0
        for idx, num in enumerate(nums):
            
            pf+=num
            ans = max(ans,ceil(pf/(idx+1)))
        return ans
        
        