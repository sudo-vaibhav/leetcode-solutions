class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        hp = []
        ans = 0
        for u,v in intervals:
            while hp and hp[0]<u:
                heappop(hp)
            heappush(hp,v)
            ans = max(ans,len(hp))
        return ans