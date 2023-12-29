class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def solve(i,j,k):
            if k==-1:return False
            if i>=j:
                return True
            if s[i]==s[j]:
                return solve(i+1,j-1,k)
            return solve(i+1,j,k-1) or solve(i,j-1,k-1)
            # return False
        return solve(0,len(s)-1,k)