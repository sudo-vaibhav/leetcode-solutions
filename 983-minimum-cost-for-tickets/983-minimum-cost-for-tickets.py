class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        
        # cost map
        cost = {
            1:costs[0],
            7:costs[1],
            30:costs[2]
        }
        

        @cache
        def s(i):
            if i==N:
                return 0
            else:
                minimumCost = inf # very large number
                for ticketType in cost.keys(): # 1,7, 30 - all kinds of passes
                    I = i # I will eventually store the first time my current pass wont work
                    # I can at most be N
                    lastDayPassWillWork = days[i]+ticketType-1
                    while I<N and days[I]<=lastDayPassWillWork:
                        I+=1
                    currentPassCost = cost[ticketType] 
                    minimumCost = min(minimumCost,currentPassCost+s(I))
                return minimumCost

        return s(0)