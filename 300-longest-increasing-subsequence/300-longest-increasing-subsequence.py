class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for v in nums:
            temp = bisect_left(res,v)
            if temp==len(res):
                res.append(v)
            else:
                res[temp]=v
        return len(res)