class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        ans = -1
        for i in s:
            if -i in s:
                ans = max(ans,abs(i))
        return ans