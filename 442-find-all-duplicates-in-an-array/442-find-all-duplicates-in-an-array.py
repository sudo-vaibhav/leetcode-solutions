# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         ans = []
#         temp = set()
#         for i in nums:
#             if i not in temp:
#                 temp.add(i)
#             else:
#                 ans.append(i)
#         return ans

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans,n = set(),len(nums)
        for i in range(n):
            while True:
                if i==nums[i]-1:
                    break
                if nums[i]==nums[nums[i]-1]:
                    ans.add(nums[i])
                    break
                a,b = nums[i],nums[nums[i]-1]
                nums[i],nums[a-1] = b,a
                
        return ans