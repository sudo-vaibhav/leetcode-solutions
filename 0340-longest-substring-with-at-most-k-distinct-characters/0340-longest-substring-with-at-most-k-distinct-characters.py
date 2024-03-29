class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        ans = 0
        d = defaultdict(int)
        for r in range(n):
            d[s[r]]+=1
            while len(d)>k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            
            ans = max(ans,r-l+1)
        return ans