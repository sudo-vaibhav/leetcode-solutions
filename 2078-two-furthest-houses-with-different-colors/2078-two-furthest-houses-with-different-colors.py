class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for f in range(n):
            for s in range(f+1,n):
                if colors[f]!=colors[s]:
                    ans = max(ans,s-f)
        return ans