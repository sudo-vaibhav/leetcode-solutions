class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # i = 0
        n = len(nums)
        for i in range(n):
            
            while 0<=nums[i]<n and nums[i]!=i and nums[i]!=nums[nums[i]]:
                v = nums[i]
                nums[v],nums[i] = v,nums[v]
        
        for i in range(n):
            if nums[i]!=i:
                return i
        # print(nums)
        
        return n