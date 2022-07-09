class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s[:] = s[::-1]
        n = len(s)
        i = 0
        
        while i<n:
            j = i
            while j<n and s[j]!=" ":
                j+=1
            s[i:j] = s[i:j][::-1]
            i=j+1
        
        