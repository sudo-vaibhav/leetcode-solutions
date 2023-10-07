class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # if n==1:
        #     if k!=0:
        #         return 0
        #     return m
        MOD = 10**9+7
        @cache
        def solve(i,deviations,prevMax):
            if i==n:return int(deviations==0)
            ans = 0
            for curVal in range(1,m+1):
                if prevMax<curVal:
                    ans+=solve(i+1,deviations-1,curVal)
                else:
                    ans+=solve(i+1,deviations,prevMax)
            ans = ans%MOD
            return ans
                
        ans = 0
        # for firstElem in range(1,m+1):
        ans+=solve(0,k,-1)
        return ans