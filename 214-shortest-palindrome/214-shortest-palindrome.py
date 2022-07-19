class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        def kmp(string):
            n = len(string)
            lps = [0]*n
            i,l = 1,0
            while i<n:
                if string[i]==string[l]:
                    l+=1
                    lps[i]=l
                    i+=1
                else:
                    if l>0:
                        l = lps[l-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        
        toAdd = len(s)-kmp(s+"#"+s[::-1])[-1]
        
        return s[-toAdd:][::-1]+s