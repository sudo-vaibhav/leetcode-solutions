class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r
        def isPos(guess):
            capLeft = guess
            daysLeft = days-1
            for i in range(len(weights)):
                cur = weights[i]
                if capLeft>=cur:
                    capLeft-=cur
                else:
                    daysLeft-=1
                    capLeft = guess-cur
                    
            return daysLeft>=0
        while l<=r:
            guessWt = l+(r-l)//2
            verdict = isPos(guessWt)
            # print(guessWt,verdict)
            if verdict==True:
                ans = min(ans,guessWt)
                r = guessWt-1
            else:
                l = guessWt+1
        
        return ans