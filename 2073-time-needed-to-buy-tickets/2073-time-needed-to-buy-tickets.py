class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        
        while True:
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    t+=1
                if tickets[k]==0:
                    return t
        # return t