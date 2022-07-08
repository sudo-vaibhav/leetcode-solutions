class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:return 0
        dist = defaultdict(int)
        n = len(s)
        l,r = 0,0
        ans = 0
        while r<n:
            while len(dist)>k:
                dist[s[l]]-=1
                if dist[s[l]]==0:
                    del dist[s[l]]
                l+=1
            dist[s[r]]+=1
            if len(dist)<=k:
                ans = max(ans,r-l+1)
            r+=1
        return ans
            