# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         t = sorted(nums)
#         l,r = inf,-inf
#         for idx in range(len(nums)):
#             if t[idx]!=nums[idx]:
#                 if idx<l:
#                     l = idx
#                 if idx>r:
#                     r = idx
#         if r-l+1>0:
#             return r-l+1
#         return 0
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<n:
            if l<n-1 and nums[l+1]<nums[l]:
                break
            else:
                l+=1
        while r>=0:
            if r>0 and nums[r]<nums[r-1]:
                break
            else:
                r-=1
        if r-l+1<0:
            return 0
        else:
            # print("lr",l,r)
            mi,ma = min(nums[l:r+1]),max(nums[l:r+1])
            L,R = l,r
            while l-1>=0:
                if nums[l-1]>mi:
                    L = l-1
                l-=1
                
            while r+1<n:
                if nums[r+1]<ma:
                    R = r+1
                r+=1
            # print("mima",mi,ma)
            return R-L+1
            