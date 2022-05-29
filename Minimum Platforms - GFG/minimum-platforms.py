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
        arr.sort()
        dep.sort()
        arrive,leave = 0,0
        ans,cur = 0,0
        while arrive<n:
            if arr[arrive]<=dep[leave]:
                cur+=1
                arrive+=1
            else:
                leave+=1
                cur-=1
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