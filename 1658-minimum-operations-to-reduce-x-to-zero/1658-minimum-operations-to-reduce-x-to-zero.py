class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        tailend = {0:n}
        s = 0
        for idx in range(n-1,-1,-1):
            cur = nums[idx]
            s+=cur
            tailend[s]=idx
        
        s = 0
        ans = inf if x not in tailend else n-tailend[x]
        for idx in range(n):
            s+=nums[idx]
            left = x-s
            if left in tailend and tailend[left]>idx:
                ans = min(ans,idx+1+n-tailend[left])
        return ans if ans!=inf else -1