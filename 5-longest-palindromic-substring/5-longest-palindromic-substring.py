class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        def equalsCount(l,r):
            diff = 0
            while l-diff>=0 and r+diff<len(s) and s[l-diff]==s[r+diff]:
                diff+=1
            return diff
            
        for startingPoint in range(len(s)):
            oddLen = equalsCount(startingPoint,startingPoint)
            evenLen = equalsCount(startingPoint,startingPoint+1)
            if 2*oddLen-1>len(ans):
                ans = s[startingPoint-oddLen+1:startingPoint+oddLen]
            if 2*evenLen>len(ans):
                ans = s[startingPoint-evenLen+1:startingPoint+evenLen+1]
                # max(ans,2*oddLen-1,2*evenLen)
        
        return ans