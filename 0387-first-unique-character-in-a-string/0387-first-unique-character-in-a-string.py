class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        
        ans = inf
        for i in ct:
            if ct[i]==1:
                ans = min(ans,s.index(i))
        
        return -1 if ans==inf else ans
            