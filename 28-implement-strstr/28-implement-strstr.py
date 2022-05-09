# KMP
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         def getLPS(s):
#             n = len(s)
#             lps = [0]*n
#             i,Len = 1,0
            
#             while i<n:
#                 if s[i]==s[Len]:
#                     Len+=1
#                     lps[i]=Len
#                     i+=1
#                 else:
#                     if Len>0:
#                         Len = lps[Len-1]
#                     else:
#                         lps[i]=0
#                         i+=1
#             return lps
#         kmp = getLPS(needle+"#"+haystack)
        
#         for i in range(len(kmp)):
#             if kmp[i]==len(needle):
#                 return i-len(needle)*2
#         return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getZArr(s):
            n = len(s)
            z = [0]*n
            l,r=0,0
            for i in range(1,n):
#                 take headstart from known region
                if i<=r:
                    z[i] = min(r-i+1,z[i-l])
#               get value from unknown region
                while i+z[i]<n and s[i+z[i]]==s[z[i]]:
                    z[i]+=1
            
#             expand known region
                if i+z[i]-1>r:
                    l = i
                    r = i+z[i]-1
            return z
        temp = needle+"#"+haystack
        zArr = getZArr(temp)
        print(temp)
        print(zArr)
        
        for idx in range(len(zArr)):
            if zArr[idx]==len(needle):
                return idx-len(needle)-1
        return -1