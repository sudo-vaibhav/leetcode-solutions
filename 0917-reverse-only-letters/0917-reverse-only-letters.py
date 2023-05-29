class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        
        i,j = 0,len(s)-1
        
        while i<len(s):
            while j>=0 and not s[j].isalpha():
                j-=1
            while i<len(s) and not s[i].isalpha():
                i+=1
            # print(i,j,ans,s)
            if i<len(s):
                ans[i]=s[j]
                j-=1
                i+=1
        return "".join(ans)
        