class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getLPS(s):
            n = len(s)
            lps = [0]*n
            i,Len = 1,0
            
            while i<n:
                if s[i]==s[Len]:
                    Len+=1
                    lps[i]=Len
                    i+=1
                else:
                    if Len>0:
                        Len = lps[Len-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        kmp = getLPS(needle+"#"+haystack)
        
        # print(kmp,len(needle))
        for i in range(len(kmp)):
            if kmp[i]==len(needle):
                return i-len(needle)*2
        return -1