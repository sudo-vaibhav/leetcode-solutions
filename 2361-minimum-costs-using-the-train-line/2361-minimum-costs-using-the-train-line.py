class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        
        @cache
        def solve(i):
            if i==0:
                return (0,expressCost)
            else:
                prevReg,prevExp = solve(i-1)
                return (
                    min(prevReg+regular[i-1],prevExp+express[i-1]),
                    min(prevExp+express[i-1],prevReg+regular[i-1]+expressCost)
                       )
            
        ans = []
        for i in range(1,n+1):
            ans.append(min(solve(i)))
        
        return ans