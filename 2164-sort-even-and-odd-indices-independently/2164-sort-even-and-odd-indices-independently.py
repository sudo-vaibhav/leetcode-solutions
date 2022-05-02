class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oarr,earr = [],[]
        for i in range(len(nums)):
            if i%2==0:
                earr.append(nums[i])
            else:
                oarr.append(nums[i])
        oarr.sort(reverse=True)
        earr.sort()
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                ans.append(earr[i//2])
            else:
                ans.append(oarr[i//2])
        return ans