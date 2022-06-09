class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            remain = target-cur
            f = bisect_left(nums,remain,i+1)
            
            if f<n and nums[f]==remain:
                return [i+1,f+1]
        