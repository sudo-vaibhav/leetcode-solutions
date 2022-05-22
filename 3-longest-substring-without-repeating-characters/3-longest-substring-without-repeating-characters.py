class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = set()
        n = len(s)
        l,r = 0,0
        ans = 0
        while r<n:
            cur = s[r]
            if cur not in vis:
                vis.add(cur)
                r+=1
            else:
                vis.remove(s[l])
                l+=1
            ans = max(ans,r-l)
        
        return ans