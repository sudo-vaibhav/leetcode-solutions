class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        ans = 0
        ctr = defaultdict(int)
        
        
        while r<n:
            ctr[s[r]]+=1
            
            if len(ctr)<3:
                ans = max(ans,sum(ctr.values()))
            else:
                while len(ctr)>2:
                    ctr[s[l]]-=1
                    if ctr[s[l]]==0:
                        del ctr[s[l]]
                    l+=1
            r+=1
        return ans
                    