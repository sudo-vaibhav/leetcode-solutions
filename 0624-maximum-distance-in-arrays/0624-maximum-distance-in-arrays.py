class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # totalCtr = defaultdict(int)
        mi,ma = arrays[0][0],arrays[0][-1]
        
        n = len(arrays)
        ans = 0
        for i in range(1,n):
            cur = arrays[i]
            ans = max(ans,abs(cur[-1]-mi),abs(cur[0]-ma))
            mi = min(mi,cur[0])
            ma = max(ma,cur[-1])
        return ans
            