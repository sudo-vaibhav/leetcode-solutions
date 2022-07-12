class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        for start in range(n):
            mini,maxi = nums[start],nums[start]
            for end in range(start,n):
                maxi = max(maxi,nums[end])
                mini = min(mini,nums[end])
                ans += maxi-mini
        return ans