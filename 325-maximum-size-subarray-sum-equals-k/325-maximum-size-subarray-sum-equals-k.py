class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        tot = 0
        totMap = {0:-1}
        ans = 0
        for i in range(len(nums)):
            tot += nums[i]
            left = -(k-tot)
            if left in totMap:
                ans = max(ans,i-totMap[left])
            # else:
            if tot not in totMap:
                totMap[tot]=i
        return ans
            
            