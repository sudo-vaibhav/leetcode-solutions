class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        s = [(nums[0],0)]
        ans = 0
        for i in range(1,n):
            cur = nums[i]
            if cur<s[-1][0]:
                s.append((cur,i))
        for j in range(n-1,-1,-1):
            while s and s[-1][0]<=nums[j]:
                _,vIdx = s.pop()
                ans = max(ans,j-vIdx)
            
#             for j in range(len(s)):
#                 val,valIdx = s[j]
#                 if val<=cur:
#                     ans = max(ans,i-valIdx)
#                     break
#             else:
#                 s.append((cur,i))
        return ans