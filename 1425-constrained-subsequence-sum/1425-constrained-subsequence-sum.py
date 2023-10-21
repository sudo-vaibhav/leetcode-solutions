class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hp = [] # (-sumSoFar,indexObtained)
        ans = -inf
        for i in range(n):
            while hp and i-hp[0][1]>k:
                heappop(hp)
            if hp:
                maxSumAtI = nums[i]+max(0,-hp[0][0])
                ans = max(ans,maxSumAtI)
            else:
                maxSumAtI = nums[i]
            ans = max(ans,maxSumAtI)
            heappush(hp,[-maxSumAtI,i])
        return ans