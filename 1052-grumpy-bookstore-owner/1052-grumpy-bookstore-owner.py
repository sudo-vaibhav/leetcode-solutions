class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        
        mini = 0
        data = list(zip(customers,grumpy))
        for c,g in data:
            if g==0:
                mini += c
        running = 0
        ans = mini
        for i in range(len(data)):
            if data[i][1]:    
                running += data[i][0]
            if i>=minutes:
                if data[i-minutes][1]:
                    running -= data[i-minutes][0]
            ans = max(ans,mini+running)
        return ans