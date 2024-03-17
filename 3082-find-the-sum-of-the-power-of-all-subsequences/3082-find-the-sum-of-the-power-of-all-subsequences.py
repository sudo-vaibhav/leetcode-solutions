class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        m = int(1e9) + 7
        @cache
        def calc(i, k, count):
            if k < 0:
                return 0
            if k == 0:
                return pow(2, len(nums) - count, m)
            if i == len(nums):
                return 0
            
            return (calc(i+1, k-nums[i], count+1) + calc(i+1, k, count))%m
        
        return calc(0, k, 0)