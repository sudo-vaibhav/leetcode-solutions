class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hp = []
        ans = 0
        intervals.sort(key=lambda x:x[0])
        
        for s,e in intervals:
            if hp and s>=hp[0][0]:
                heappop(hp)
            heappush(hp,(e,(s,e)))
            ans = max(ans,len(hp))
        return ans