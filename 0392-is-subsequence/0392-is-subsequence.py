class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        i = 0
        
        for k in range(0,len(t)):
            if i<len(s):
                if s[i]==t[k]:
                    i+=1
        
        return i==len(s)