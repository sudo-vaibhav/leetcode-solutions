#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meets = []
        for i in range(len(start)):
            meets.append({"start":start[i],"end":end[i]})
        
        meets.sort(key=lambda x:(x["end"]))
        prev = meets[0]
        ans = 1
        
        for meet in meets[1:]:
            if prev["end"]<meet["start"]:
                prev = meet
                ans+=1
            else:
                continue
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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends