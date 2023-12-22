# from multiset import *
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l,r = 0,0
        n = len(s)
        seen = defaultdict(int)
        ans = 0
        while r<n:
            seen[s[r]]+=1
            while len(seen)>2:
                seen[s[l]] -= 1
                if seen[s[l]]==0:
                    del seen[s[l]]
                l+=1
                
            # print(l,r,s[l:r+1])
            ans = max(ans,r-l+1)
            r+=1
        return ans