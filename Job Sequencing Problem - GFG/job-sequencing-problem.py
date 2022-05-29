#User function Template for python3
import heapq
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        arr = [(job.id,job.deadline,job.profit) for job in Jobs]
        arr.sort(key=lambda x: (x[1]))
        totProfit= 0
        # initialise the result array and maxHeap
        result = []
        maxHeap = []
        # starting the iteration from the end
        for i in range(n - 1, -1, -1):
    
            # calculate slots between two deadlines
            if i == 0:
                slots_available = arr[i][1]
            else:
                slots_available = arr[i][1] - arr[i - 1][1]
    
            # include the profit of job(as priority), deadline
            # and job_id in maxHeap
            # note we push negative value in maxHeap to convert
            # min heap to max heap in python
            heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))
    
            while slots_available and maxHeap:
    
                # get the job with max_profit
                profit, deadline, job_id = heapq.heappop(maxHeap)
    
                # reduce the slots
                slots_available -= 1
    
                # include the job in the result array
                result.append([job_id, deadline,profit])
                totProfit+=-profit
    
        # jobs included might be shuffled
        # sort the result array by their deadlines
        # result.sort(key=lambda x: x[1])
        return [len(result),totProfit]
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends