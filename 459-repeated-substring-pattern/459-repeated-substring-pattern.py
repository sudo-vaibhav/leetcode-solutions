# simple approach using string concatenation
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         return s in (s+s)[1:-1]


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def lps(lpsArray):
            i,length = 1,0
            while i<n:
                if s[length]==s[i]:
                    length+=1
                    lpsArray[i]=length
                    i+=1
                else:
                    if length>0:
                        length = lpsArray[length-1]
                    else:
                        lpsArray[i]=0
                        i+=1
            
        
        lpsArray = [0 for i in range(n)]
        lps(lpsArray)
        if lpsArray[-1]==0: return False
        temp = len(s)-lpsArray[-1]
        return s[:temp]*(n//temp)==s