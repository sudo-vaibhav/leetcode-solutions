# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = nums[0]
        while l<=r:
            m = l+(r-l)//2
            ans = min(ans,nums[m])
            if nums[l]<=nums[m]:
                ans = min(ans,nums[l])
                l = m+1
            elif nums[m]<=nums[r]:
                # ans = min(ans,nums[m])
                r = m-1
        return ans
            
            
            