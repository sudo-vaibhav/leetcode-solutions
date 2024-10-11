class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        
        r = 0
        
        for i in range(len(nums)):
            if s-r-nums[i]==r:
                return i
            r += nums[i]
        return -1