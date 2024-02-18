from sortedcontainers import SortedSet
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counts = defaultdict(int)
        
        # heap = []
        avail = SortedSet(range(n))
        # print(avail)
        usage = []
        
        for meeting in meetings:
            canStart = meeting[0]
#             some rooms would free automatically sometime due to non overlap
            while usage and usage[0][0]<=canStart:
                e, room = heappop(usage)
                avail.add(room)
            
#             for case when no room has automatically freed, so we need to wait for one
            if len(avail)==0:# or (usage and usage[0][0]<=meeting[0]):
                e, room = heappop(usage)
                avail.add(room)
                canStart = max(canStart,e)
            roomToTake = avail[0]
            # print(meeting,roomToTake,canStart)
#             if len(usage)==n:
# #                 just one pop could be a problem,might wanna pop all before current event start
                
#                 canStart = max(canStart,e)
#                 roomToTake = room
#             else:
#                 
#                 roomToTake = avail[0]
#                 avail.remove(roomToTake)
#                 heappush(usage,(ending,roomToTake))
            avail.remove(roomToTake)
            ending = canStart+(meeting[1]-meeting[0])
            heappush(usage,(ending,roomToTake))                
            counts[roomToTake]+=1
            
        # print(counts)
        f = max(counts.values())
        for i in counts:
            if counts[i]==f:
                return i
#             if avail:
#                 heappush(endingHeap,(meeting[1],avail.popleft()))
#             else:
                
#                 heappush(endingHeap,(avail.popleft()