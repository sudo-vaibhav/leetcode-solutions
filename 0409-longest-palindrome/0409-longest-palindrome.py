class Solution:
    def longestPalindrome(self, s: str) -> int:
        
#         @cache
#         def solve(i,j):
#             if i>j:
#                 return 0
#             if i==j:
#                 return 1
#             ans = max(solve(i+1,j),solve(i,j-1))
#             if s[i]==s[j]:
#                 ans = max(ans,2+solve(i+1,j-1))
#             return ans
#         return solve(0,len(s)-1)
        o = False
        ans = 0
        
        c = Counter(s)
        
        for k in c:
            if c[k]%2==0:
                ans += c[k]
            else:
                o = True
                ans += 2*(c[k]//2)
        return int(o)+ans
        