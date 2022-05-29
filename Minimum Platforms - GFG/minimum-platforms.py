#User function Template for python3
from heapq import heappush,heappop
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        depart,arrive = 0,1 
        trains = [(arr[i],dep[i]) for i in range(n)]
        trains.sort()
        
        plats = []
        
        ans = 0
        for tr in trains:
            if len(plats)==0 or plats[0][depart]>=tr[0]:
                heappush(plats,(tr[1],tr[0]))
            else:
                heappop(plats)
                heappush(plats,(tr[1],tr[0]))
            ans = max(ans,len(plats))

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