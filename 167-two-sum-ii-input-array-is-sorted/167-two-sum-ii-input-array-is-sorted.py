# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             cur = nums[i]
#             remain = target-cur
#             f = bisect_left(nums,remain,i+1)
#             if f<n and nums[f]==remain:
#                 return [i+1,f+1]
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i,j = 0,n-1
        while i<j:
            X,Y = nums[i],nums[j]
            tot = X+Y
            if tot>target:
                j-=1
            elif tot<target:
                i+=1
            else:
                return [i+1,j+1]