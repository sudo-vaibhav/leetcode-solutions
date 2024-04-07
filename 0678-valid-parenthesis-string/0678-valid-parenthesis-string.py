class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def solve(i,c):
            if c<0: return False
            if i==n:
                return c==0
            if s[i]=="(":
                return solve(i+1,c+1)
            elif s[i]==")":
                if c==0: return False
                return solve(i+1,c-1)
            else:
                return solve(i+1,c) or solve(i+1,c-1) or solve(i+1,c+1)
        
        return solve(0,0)