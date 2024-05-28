class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l,r = 0,0
        n = len(s)
        cur = 0
        ans = 0
        while r<n:
            cur += abs(ord(s[r])-ord(t[r]))
            while cur>maxCost:
                cur -= abs(ord(s[l])-ord(t[l]))
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans