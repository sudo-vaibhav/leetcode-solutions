class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        v = (2**maximumBit)-1
        t = 0
        for i in nums:
            t^=i
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(t^v)
            t^=nums.pop()
        return ans