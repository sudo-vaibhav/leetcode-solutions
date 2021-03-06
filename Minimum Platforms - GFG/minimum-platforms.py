#User function Template for python3
from heapq import heappush,heappop
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        # depart,arrive = 0,1 
        # trains = [(arr[i],dep[i]) for i in range(n)]
        # trains.sort()
        
        # plats = []
        
        # ans = 0
        # for tr in trains:
        #     if len(plats)==0 or plats[0][depart]>=tr[0]:
        #         pass # cant pop anything
        #     else:
        #         heappop(plats)
        #     heappush(plats,(tr[1],tr[0]))
        #     ans = max(ans,len(plats))

        # return ans
        
        # times = sorted([(x,"arr") for x in arr]+[(x,"dep") for x in dep])
        # cur,ans= 0,0
        # for time,timeType in times:
        #     if timeType=="arr":
        #         cur+=1
        #     else:
        #         cur-=1
        #     ans = max(ans,cur)
        trains = [0 for i in range(2361)]
        
        for time in arr:
            trains[time]+=1
            
        for time in dep:
            trains[time+1]-=1
        
        cur,ans = trains[0],trains[0]
        for i in range(1,len(trains)):
            cur += trains[i]
            ans = max(ans,cur)
            
        
        return ans
                
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends