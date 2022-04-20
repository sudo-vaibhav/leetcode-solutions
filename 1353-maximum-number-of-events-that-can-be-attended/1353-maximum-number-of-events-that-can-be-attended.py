
def dbg(*args, **kwargs):
    # return
    print(*args, file=sys.stdout, **kwargs)


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : x[0])
        # dbg(events)
        n = len(events)
        i = 0
        q = []
        cnt=0
        temp = [*[x[0] for x in events],*[x[1] for x in events]]
        min_day = min(temp)
        max_day = max(temp)
        day = min_day
        while day<max_day+1 and cnt<n:
            # print(day,q)
            if len(q)==0 and i<n:
                day = events[i][0]
            while i<n and events[i][0]<=day:
                heappush(q,(events[i][1],events[i]))
                i+=1
            while len(q)>0 and q[0][0]<day:
                heappop(q)
            if len(q)>0:
                heappop(q)
                cnt+=1
            day+=1
                
        return cnt
        