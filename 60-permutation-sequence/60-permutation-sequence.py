class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        ans = []
        while len(nums)>0:
            N = len(nums)
            perHead = factorial(N-1)
            numPickedIdx = (k-1)//perHead
            pickedNum = nums[numPickedIdx]
            ans.append(str(pickedNum))
            nums.remove(pickedNum)
            k = k%perHead
        return "".join(ans)