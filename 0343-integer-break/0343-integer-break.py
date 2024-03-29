class Solution:
    
    def integerBreak(self, n: int) -> int:
        
        @cache
        def solve(n,cnt):
            if n<=1:
                return 1
            tempans = -inf
            for i in range(1,n+(1 if cnt==True else 0)):
                tempans = max(tempans,solve(n-i,cnt or True)*i)
            return tempans
        return solve(n,False)