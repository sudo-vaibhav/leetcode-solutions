class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        
        ans = r
        def isPos(m):
            hoursUsed = 0
            for i in range(len(piles)):
                hoursUsed+= ceil(piles[i]/m)
            return hoursUsed<=h
        while l<=r:
            guess = l+(r-l)//2
            if isPos(guess):
                ans = min(ans,guess)
                r = guess-1
            else:
                l = guess+1
        
        return ans