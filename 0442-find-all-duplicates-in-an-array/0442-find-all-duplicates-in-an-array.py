class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            idx = val-1
            if nums[idx]<0:
                ans.append(idx+1)
            nums[idx] = -abs(nums[idx])
        for i in range(n):
            nums[idx] = abs(nums[idx])
        return ans
                