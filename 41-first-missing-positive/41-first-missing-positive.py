class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
#         thumb rule, positive number j should be present at index j-1
        i,n = 0,len(nums)
        
        while i<n:
            if nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                temp = nums[nums[i]-1]
                cur = nums[i]
                nums[i],nums[cur-1] = temp,cur
            else:
                i+=1
        for i in range(0,n):
            if nums[i]!=i+1:
                return i+1
        
        return n+1