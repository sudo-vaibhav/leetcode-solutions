class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            t = []
            for i in range(1,len(nums)):
                t.append((nums[i]+nums[i-1])%10)
            nums = t
            
        return nums[0]