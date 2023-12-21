class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        r = sorted([p[0] for p in points])
        
        ans = 0
        
        for i in range(1,len(r)):
            ans = max(ans,r[i]-r[i-1])
        return ans