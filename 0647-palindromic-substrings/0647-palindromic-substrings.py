class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        @cache
        def isPalin(i,j):
            if i>j : return True
            if i==j: return True
            return s[i]==s[j] and isPalin(i+1,j-1)
        
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if isPalin(i,j):
                    ans +=1
        return ans