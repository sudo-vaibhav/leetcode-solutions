class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum,maxSum = nums[0],nums[0]
        for elem in nums[1:]:
            if curSum<0:
                curSum=0
            curSum+=elem
            maxSum = max(maxSum,curSum)
        return maxSum