class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        ans = []
        def solve(k):
            N = len(nums)
            if N==0:return
            totalPerms = factorial(N)
            perHead = totalPerms//N
            
            numPickedIdx = (k-1)//perHead
            pickedNum = nums[numPickedIdx]
            ans.append(str(pickedNum))
            nums.remove(pickedNum)
            newK = k%perHead
            solve(newK)
            
            
        solve(k)
        return "".join(ans)