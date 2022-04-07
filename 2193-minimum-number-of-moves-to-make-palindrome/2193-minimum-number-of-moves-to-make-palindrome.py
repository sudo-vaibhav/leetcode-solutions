class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        n = len(s)
        l,r=0,n-1
        ans=0
        while l<r:
            if s[l]==s[r]:
                l,r=l+1,r-1
            else:
                k=r
                while k>l and s[l]!=s[k]:
                    k-=1
                if k==l:
                    s[k],s[k+1]=s[k+1],s[k]
                    ans+=1
                else:
                    while k<r:
                        s[k],s[k+1]=s[k+1],s[k]
                        k+=1
                        ans+=1
                    l+=1
                    r-=1
        return ans