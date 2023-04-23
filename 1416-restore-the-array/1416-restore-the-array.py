class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        MOD = 10**9+7
        @cache
        def solve(i):
            if i==n:return 1
            ans = 0
            
            if s[i]=="0": return 0
            numSoFar = 0
            for j in range(i,n):
                numSoFar *= 10
                numSoFar+=int(s[j])
                if numSoFar>k:break
                ans+= solve(j+1)
                if ans>=MOD:ans-=MOD
            return ans
        
        return solve(0)
        