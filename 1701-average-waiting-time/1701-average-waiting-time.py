class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = 0
        ans = 0
        for a,t in customers:
            if a>curTime:
                curTime = a
#             elif a<curTime:
#                 ans += curTime-a
                
            finishTime = curTime+t
            ans += finishTime-a
            curTime = finishTime
        return ans/len(customers)