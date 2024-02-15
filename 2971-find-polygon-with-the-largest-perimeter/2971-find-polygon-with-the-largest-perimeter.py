class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        sumSoFar = nums[0]+nums[1]
        ans = -1
        for s in nums[2:]:
            if sumSoFar>s:
                ans = max(ans,sumSoFar+s)
            sumSoFar+=s
        return ans