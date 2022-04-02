class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        
        def solve(l,r,m):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    if m==0:
                        return False
                    return solve(l+1,r,m-1) or solve(l,r-1,m-1)
            return True  
                
        return solve(l,r,1)