class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        ans = 0
        end,start = 0,1
        intervals.sort()
        for interval in intervals:
            if len(rooms)==0 or rooms[0][end]>interval[0]:
                pass
            else:
                heappop(rooms)
            heappush(rooms,(interval[1],interval[0]))
                
            ans = max(ans,len(rooms))
        
        return ans