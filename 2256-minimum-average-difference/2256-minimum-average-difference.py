class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        soFar = 0
        minIdx,minVal = -1,inf
        tot = sum(nums)
        for i in range(n):
            soFar+= nums[i]
            otherSide = tot - soFar
            l = soFar//(i+1)
            r = (otherSide//(n-i-1)) if n-i-1>0 else 0
            temp  = abs(l-r)
            if temp<minVal:
                minVal = temp
                minIdx = i
        return minIdx