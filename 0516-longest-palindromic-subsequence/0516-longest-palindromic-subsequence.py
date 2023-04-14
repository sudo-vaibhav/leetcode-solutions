class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def solve(l,r):
            if l>r:return 0
            elif l==r: return 1
            else:
                L,R = s[l],s[r]
                
                if L==R:
                    return 2+solve(l+1,r-1)
                else:
                    return max(solve(l+1,r),solve(l,r-1))
        
        return solve(0,len(s)-1)