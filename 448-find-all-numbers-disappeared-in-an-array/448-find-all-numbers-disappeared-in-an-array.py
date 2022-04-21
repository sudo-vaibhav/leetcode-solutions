# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         nums = set(nums)
#         ans = []
#         for i in range(1,n+1):
#             if i not in nums:
#                 ans.append(i)
#         return ans

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # nums = set(nums)
        ans = []
        for i in range(0,n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                a,b = nums[i],nums[nums[i]-1]
                nums[i],nums[a-1] = b,a
                # print(nums)
                
        for i in range(0,n):
            if nums[i]!=i+1:
                ans.append(i+1)
        return ans