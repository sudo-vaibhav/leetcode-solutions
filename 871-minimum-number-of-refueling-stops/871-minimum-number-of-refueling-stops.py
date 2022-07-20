class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        n = len(stations)
        position,fuel = 0,1
#         l,r = 0,n
        
#         while l<=r:
#             mid = l+(r-l)//2
#             toCover = max(0,target-startFuel)
# #             returns the max distance you can go if you take k stops
#             @cache
#             def solve(i,stopsLeft):
#                 if i==n:
#                     return 0
#                 ans = solve(i+1,)
                
            
#             if solve(0,mid)>=toCover:
#                 ans = min(ans,mid)
#                 r = mid-1
#             else:
#                 l = mid+1
        
#         return ans

        
        heap = []
        stationIter = 0
        covered = startFuel
        while stationIter<n and stations[stationIter][position]<=covered:
            heappush(heap,(-stations[stationIter][fuel]))
            stationIter+=1
        while covered<target and heap:
            covered+= -heappop(heap)
            ans += 1
            # if 
            while stationIter<n and stations[stationIter][position]<=covered:
                heappush(heap,(-stations[stationIter][fuel]))
                stationIter+=1
        
        if covered<target:
            return -1
        return ans