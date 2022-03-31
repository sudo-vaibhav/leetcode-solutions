class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n=len(nums)
        prefixSum = [0]+list(itertools.accumulate(nums))
        # print(prefixSum)
        
        @cache
        def solve(idx,subA):
            if subA == 1:
                return prefixSum[n]-prefixSum[idx]
            tempans = prefixSum[n]
            
            for endCurAt in range(idx,n-(subA-1)):
                firstSum = prefixSum[endCurAt+1]-prefixSum[idx]
                tempans = min(
                    tempans,
                      max(
                        firstSum,
                        solve(endCurAt+1,subA-1)
                      )
                )
                if firstSum>tempans:
                    break
            return tempans
        
        return solve(0,m)