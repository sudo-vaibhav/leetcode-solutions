class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curStreak = 1
        ans = 0
        s = lambda n:(n*(n+1))//2
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                curStreak+=1
            else:
                ans += s(curStreak)
                curStreak = 1
        ans += s(curStreak)
        return ans
                