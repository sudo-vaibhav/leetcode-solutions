class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        sumOfSmaller = 0
        totalSum = sum(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            val = i*nums[i]-sumOfSmaller
            val += (totalSum-sumOfSmaller-nums[i])-(n-1-i)*nums[i]
            sumOfSmaller += nums[i]
            ans.append(val)
        return ans