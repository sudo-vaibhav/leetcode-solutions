class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # ans = 0
        
        # for i in range(len(tickets)):
        #     ans += 
            
        return sum(min(tickets[k]-int(i>k),tickets[i]) for i in range(len(tickets)))