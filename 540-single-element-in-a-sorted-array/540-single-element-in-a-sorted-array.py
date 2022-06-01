class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-2
#         if all were appearing twice, first occurence of num occurs in even position
#         and second occurence occurs in odd position
        while l<=r:
            mid = l+(r-l)//2
            cur = nums[mid]
            if nums[mid]==nums[mid^1]:
                l = mid+1
            else:
                r = mid-1
#             if mid>0 and nums[mid-1]==cur:
# #                 this is second occurence
#                 if mid%2==0:
# #         outlier lies behind
#                     r = mid-1
#                 else:
#                     l = mid+1
#             elif mid<len(nums)-1 and nums[mid+1]==cur:
#                 if mid%2==1:
#                     r = mid-1
#                 else:
#                     l = mid+1
            # else:
                # return nums[mid]
            
            
        
        return nums[l]