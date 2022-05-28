class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # i = 0
        n = len(nums)
#         for i in range(n):
            
#             while 0<=nums[i]<n and nums[i]!=i and nums[i]!=nums[nums[i]]:
#                 v = nums[i]
#                 nums[v],nums[i] = v,nums[v]
        
#         for i in range(n):
#             if nums[i]!=i:
#                 return i
        
#         return n


        S = sum(nums)
        
        temp = (n*(n+1))//2
        diff = temp-S
        if diff==0:
            return 0
        else:
            return diff
        
        return n