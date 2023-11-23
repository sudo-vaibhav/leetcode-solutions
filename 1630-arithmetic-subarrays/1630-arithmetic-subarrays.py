class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        prev = nums[1]-nums[0]
        # prevIdx = 0
        lastChange = [0]
        for i in range(1,n):
            diff = nums[i]-nums[i-1]
            if diff!=prev:
                lastChange.append(i-1)
                prev = diff
                # prevIdx
            else:
                lastChange.append(lastChange[-1])
        ans = []
        for L,R in zip(l,r):
            temp = list(sorted(nums[L:R+1]))
            diff = temp[1]-temp[0]
            for i in range(1,len(temp)):
                if temp[i]-temp[i-1]!=diff:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        # print(lastChange)
        return ans