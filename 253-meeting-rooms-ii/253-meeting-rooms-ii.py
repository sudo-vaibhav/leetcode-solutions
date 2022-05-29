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


# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         times = sorted([(x[0],"start") for x in intervals]+[(x[1],"end") for x in intervals])
#         cur,ans= 0,0
#         for time,timeType in times:
#             if timeType=="start":
#                 cur+=1
#             else:
#                 cur-=1 # end gets removed before due to end being lexicographically smaller than start
#             ans = max(ans,cur)
#         return ans
                