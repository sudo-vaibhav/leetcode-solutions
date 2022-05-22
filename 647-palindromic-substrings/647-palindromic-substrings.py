class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def countPalin(i,j):
            res = 0
            while i>=0 and j<n:
                if s[i]==s[j]:
                    res+=1
                    i-=1
                    j+=1
                else:
                    break
            return res
        
        ans = 0
        
        for i in range(n):
            ans += countPalin(i,i)
            ans += countPalin(i,i+1)
        
        return ans