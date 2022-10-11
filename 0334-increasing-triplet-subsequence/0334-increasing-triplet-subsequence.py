class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        maxs = [nums[-1]]*n
        if n<3:return False
        for i in range(n-2,-1,-1):
            maxs[i] = max(nums[i],maxs[i+1])
        prevMin = nums[0]
        for i in range(1,n-1):
            cur = nums[i]
            if prevMin < cur < maxs[i+1]:
                return True
            prevMin = min(prevMin,cur)
        return False