class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def solve(i):
            if i>n:
                return 0
            elif i==n:
                return 1
            else:
                ans = 0
#                 try 1
                if s[i]!="0":
                    ans+= solve(i+1)
                
#                 try 2
                if i<n-1 and s[i]!="0" and int(s[i:i+2])<=26:
                    ans+=solve(i+2)
                return ans
                    
                
                
        return solve(0)