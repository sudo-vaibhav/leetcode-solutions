class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while True:
                val = nums[i]
                if val<=0 or val>n or val==i+1:
                    break
                else:
                    if nums[val-1]==nums[i]:break
                    nums[val-1],nums[i] = nums[i],nums[val-1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
                
        return n+1