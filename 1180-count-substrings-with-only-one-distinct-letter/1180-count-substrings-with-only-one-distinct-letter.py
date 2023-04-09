class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        i = 0
        ans = 0
        while i<n:
            j = i
            c= 0
            while j<n:
                if s[i]==s[j]:
                    c+=1
                else:
                    break
                j+=1
            i=j
            ans+=(c*(c+1))//2
        return ans