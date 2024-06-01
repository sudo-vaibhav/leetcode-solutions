class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1,len(s)):
            prev,cur = s[i-1],s[i]
            
            ans += abs(ord(prev)-ord(cur))
        return ans