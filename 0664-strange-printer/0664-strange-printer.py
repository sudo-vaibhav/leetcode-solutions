class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def solve(l,r):
            if l>r: return 0
            ans = n
            firstUnequal = None
            for paintTill in range(l,r):
                if s[paintTill]!=s[r] and firstUnequal is None:
                    firstUnequal = paintTill
                    
                if firstUnequal is not None:
                    ans = min(ans,
                      1
                      +solve(firstUnequal,paintTill)
                      +solve(paintTill+1,r)
                    )
            if firstUnequal is None: return 0
            return ans
                    
            
            
        return solve(0,n-1)+1