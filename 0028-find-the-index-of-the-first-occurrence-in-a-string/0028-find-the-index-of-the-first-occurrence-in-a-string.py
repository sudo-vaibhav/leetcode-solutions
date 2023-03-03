class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def solve(s):
            n = len(s)
            ans = [0]*n
            i,l = 1,0
            while i<n:
                if s[i]==s[l]:
                    l+=1
                    ans[i]=l
                    i+=1
                else:
                    if l>0:
                        l = ans[l-1]
                    else:
                        # lps[i]
                        i+=1
            return ans
        
            # for i in range(1,n):
                
                
        lps = solve(needle+"#"+haystack)
        # print(lps)
        for idx,i in enumerate(lps):
            if i==len(needle):
                return idx-len(needle)*2
        
        return -1