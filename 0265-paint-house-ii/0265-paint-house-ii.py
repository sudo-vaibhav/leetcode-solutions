class Solution:
    def minCostII(self, c: List[List[int]]) -> int:
        
        n,k = len(c),len(c[0])
        
        @cache
        def solve(hIdx,prevCol=-1):
            if hIdx==n: return 0     
            ans = inf
            for col in range(k):
                if col!=prevCol:
                    ans = min(ans,c[hIdx][col]+solve(hIdx+1,col))
            return ans
            
        
        return solve(0)